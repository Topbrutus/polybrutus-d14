#!/usr/bin/env python3
"""Independent Polybrutus D14 labelled-metric and spectrum verification.

DOES NOT import any symbolic point generator. Computes exact rational
squared distances from the original 7 canonical points, the 5 regular
simplex points and 7 additional orthogonal unit-axis points.
"""
from pathlib import Path
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
import hashlib,json
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
report=json.loads((ROOT/"results"/"certificate_d14.json").read_text(encoding="utf8"))
parent=json.loads((ROOT/"prior"/"certificate_d13.json").read_text(encoding="utf8"))
core=[
 (F(0),F(0),F(1)),(F(1,2),F(0),F(1,2)),
 (F(-1,4),F(3,4),F(1,2)),(F(-1,4),F(-3,4),F(1,2)),
 (F(0),F(0),F(-1)),(F(1,2),F(0),F(-1,2)),
 (F(-1,2),F(0),F(-1,2))
]
def squared_distance(i,j):
    if i==j:return F(0)
    if i<7 and j<7:
        a,b,c=(core[i][k]-core[j][k] for k in range(3))
        return 3*a*a+b*b+c*c
    if 7<=i<12 and 7<=j<12:return F(5,2)
    return F(2)

pairs=list(combinations(range(19),2))
exact={(i+1,j+1):squared_distance(i,j) for i,j in pairs}
published={(int(e["i"]),int(e["j"])):F(e["d2"])
           for e in report["labelled_squared_distances"]}
assert len(exact)==171 and exact==published
old={(int(e["i"]),int(e["j"])):F(e["d2"])
     for e in parent["labelled_squared_distances"]}
assert len(old)==153 and all(exact[k]==v for k,v in old.items())
assert all(squared_distance(i,18)==F(2) for i in range(18))
hist=Counter(4*squared_distance(i,j) for i,j in pairs)
assert hist==Counter({F(4):6,F(7):2,F(8):140,F(9):3,F(10):10,F(12):6,F(13):2,F(16):2})
assert sum(exact.values(),F(0))==F(1415,4)
D=s.Matrix(19,19,lambda i,j:s.Rational(squared_distance(i,j).numerator,squared_distance(i,j).denominator))
H=s.eye(19)-s.ones(19)/19
B=-H*D*H/2
assert B.rank()==14
D13=D[:18,:18];H13=s.eye(18)-s.ones(18)/18
assert (-H13*D13*H13/2).rank()==13

L=s.zeros(19)
for i,j in pairs:
    w=1/D[i,j]
    L[i,i]+=w;L[j,j]+=w
    L[i,j]-=w;L[j,i]-=w
z=s.Symbol("z");charpoly=L.charpoly(z).as_expr()
for value,multiplicity in [(s.Rational(19,2),8),(s.Integer(9),4)]:
    assert all(s.simplify(s.diff(charpoly,z,k).subs(z,value))==0 for k in range(multiplicity))
    assert s.simplify(s.diff(charpoly,z,multiplicity).subs(z,value))!=0
assert report["affine_rank"]==report["centered_gram_rank"]==14
assert report["parent_distances_preserved"]==153 and report["new_distances"]==18
p=ROOT/"results"/"certificate_d14.json"
print("INDEPENDENT D14 PASS: 171 rational labelled distances; 153 previous preserved; Gram rank 14")
print("INDEPENDENT IDEAL GRAPH PASS: eigenvalue 19/2 x8; eigenvalue 9 x4")
print("CERTIFICATE_SHA256="+hashlib.sha256(p.read_bytes()).hexdigest())

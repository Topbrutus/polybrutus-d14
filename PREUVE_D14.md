# Polybrutus 14D — Exact Euclidean distance and spectrum certificate

## 1. Conservative labelled metric

Begin with the frozen labelled eighteen-point Polybrutus D13, whose unit vectors all have norm 1 and whose exact metric has `C(18,2)=153` pairs. Append a zero coordinate to each point. Add the new unit vector `e15`, orthogonal to all eighteen old vectors.

Old point-to-point distances are identical. Every newly introduced squared distance satisfies

```
||e15-(p_i,0)||² = ||e15||²+||p_i||²-2<e15,p_i> = 2,
i=1,...,18.
```

Hence there are exactly `153+18=171` labelled pairs, histogram `{4:6,7:2,8:140,9:3,10:10,12:6,13:2,16:2}` for `k=4d²`, and the squared-distance sum is `1415/4`.

## 2. Minimal Euclidean affine dimension exactly 14

Let `X` be the exact 19-by-15 coordinate array, `D` the exact 19-by-19 squared-distance matrix and `H=I-11ᵀ/19` the centered projection.

The exact symbolic program checks all three statements independently:

```
rank([q2-q1,...,q19-q1]) = 14
rank(B) = 14
B = -H D H / 2 = (H X)(H X)^T
```

The final exact factorization proves `B` positive semidefinite. As the labeled metric uniquely determines the centered Gram matrix, **every Euclidean realization of these exact 171 labelled squared distances has affine rank 14**, despite the coordinate storage's fifteen slots and one simplex-hyperplane linear relation.

## 3. Selected weighted-Laplacian scalar-oscillator model

For a mathematical complete graph on the nineteen vertices, choose equal unit masses and weights `w_ij=1/d_ij²`. The new vertex joins eighteen old vertices uniformly with weight 1/2. Let `L13` be the previous eighteen-vertex graph Laplacian. Then:

```
L14 = [ L13 + (1/2) I18  -(1/2) 1 ]
      [ -(1/2) 1ᵀ               9  ].
```

The monic characteristic polynomial obeys

```
chi19(z) = z(z-19/2) chi18(z-1/2)/(z-1/2).
```

The frozen D13 result has `chi18(z)=z(z-9)^7(z-17/2)^4 f6(z-11/2)`, where `f6=chiP7/z` describes the original seven-point graph's six nonuniform modes. Substitution yields

```
chi19(z)=z(z-19/2)^8(z-9)^4 f6(z-6).
```

The source verifies equality with the directly computed **19-by-19 exact characteristic polynomial**, and checks `f6(7/2)!=0`, `f6(3)!=0`, ruling out additional multiplicities. Thus the precise multiplicities are **eight** at 19/2 and **four** at 9.

A separate rational-metric program independently computes all 171 labelled values, the rank-14 Gram matrix and the full nineteen-vertex characteristic polynomial. It checks both multiplicities via polynomial derivatives, without importing the primary generator.

## 4. Negative controls and limitations

Four intentionally incorrect test cases are rejected: corrupting a distance, duplicating the last vertex, tilting the last vector toward the original geometry, and swapping labels while keeping the multiset of unlabelled distances identical.

Orthogonal extensions and uniform graph joins are established mathematics. This **particular computable case** is not evidence of an unknown physical spacetime dimension, a new general theorem, a physical resonance or a particle discovery. No independent human peer review has occurred.

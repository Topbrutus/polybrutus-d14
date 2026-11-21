# Polybrutus 14D — Exact nineteen-point Euclidean configuration

**Frozen predecessor:** `Topbrutus/polybrutus-d13@v0.1.0`, commit `4d5f10de586e6677ddbe1d90b18218b46602d14e`, DOI `10.5281/zenodo.24408769`.

## Coordinates and rank

At radius one, let `p1,...,p18` be the frozen D13 vectors in 14 storage-coordinate slots. The original five-vertex centered-simplex block obeys one exact linear constraint.

Embed all old vertices `q_i=(p_i,0)` for `1<=i<=18`. Append `q19=e15=(0,...,0,1)` in the 15th storage coordinate. The newly adjoined point is orthogonal to all preceding points and has norm one.

```
d(q_i,q19)^2 = 2,   for i=1,...,18.
```

For any `R>0`, multiply all vectors by `R`; the new squared lengths become `2R²`. All 153 predecessor labelled distances remain unchanged. The **15 storage coordinates** obey a single constraint, giving intrinsic **affine rank 14**.

### Exact squared-distance families

For `k=4d²/R²`:

| k | 4 | 7 | 8 | 9 | 10 | 12 | 13 | 16 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Count | 6 | 2 | **140** | 3 | 10 | 6 | 2 | 2 |

There are `C(19,2)=171` labelled unordered pairs and `sum(d_ij²) = 1415 R²/4`.

At radius one, the storage-coordinate centroid is `(0,0,1/38,0,0,0,0,0,1/19,1/19,1/19,1/19,1/19,1/19,1/19)`.

### Ideal oscillator graph

Choose complete coupling weights `w_ij=R²/d_ij²` and unit scalar masses. All 18 new couplings have weight 1/2, yielding the 19-by-19 Laplacian block identity:

```
L14 = [ L13 + (1/2) I18      -(1/2) 1 ]
      [ -(1/2) 1ᵀ                  9  ].
```

The exact characteristic polynomial factors as:

```
chi19(z) = z(z-19/2)^8(z-9)^4 f6(z-6),
f6(z) = chiP7(z)/z.
```

Eigenvalue 19/2 has multiplicity 8; eigenvalue 9 has multiplicity 4. These are exact **mathematical graph-model** eigenvalues, not physical measurements.

# Polybrutus 14D: Exact Conservative Euclidean Completion and an Eightfold Weighted-Graph Mode

**Research author:** Gabriel St-Pierre  
**Affiliation:** Independent researcher  
**Project:** Polybrutus-X72  
**Date:** 20 November 2026  
**Version:** 0.1.0  
**Status:** Computational mathematical preprint, not independently peer reviewed  
**Predecessor:** Polybrutus 13D, DOI 10.5281/zenodo.24408769  
**Frozen source:** https://github.com/Topbrutus/polybrutus-d14/tree/v0.1.0 (upon release)

## Abstract

A labelled **nineteen-point Euclidean distance configuration** with minimal affine embedding dimension **fourteen** is constructed exactly from the certified Polybrutus 13D metric. All **153 predecessor labelled squared distances** are preserved, and one newly added orthogonal radius-one vector contributes **18 new pairwise squared distances of exactly 2R²**. The resulting complete metric has **171 pairwise distances**, divided into eight exact normalized distance classes. Exact symbolic computations prove the affine rank fourteen both from coordinate differences and from the centered Euclidean-distance Gram matrix, including an explicit positive-semidefinite factorization. A separately implemented rational-arithmetic verifier independently reconstructs all 171 labelled distances and the Gram rank.

For a deliberately **chosen ideal scalar-oscillator complete graph** with couplings `w_ij=R²/d_ij²`, the exact characteristic polynomial exhibits an **eightfold eigenvalue at 19/2** and a **fourfold eigenvalue at 9**. These properties are independently checked by two programs. The work is a reproducible mathematical case study based on known orthogonal-extension and graph spectral techniques, **not** evidence for a previously unknown physical dimension, a novel universal theorem or measured frequencies.

## 1. Frozen research provenance

Polybrutus begins with seven analytically defined radius-R points on a three-dimensional sphere. A first exact seven-dimensional completion added five vertices of a regular four-dimensional simplex in a perpendicular subspace, producing twelve vertices and sixty-six pairwise squared distances while preserving the canonical seven-point geometry (DOI **10.5281/zenodo.24407952**).

A chain of individually archived computational cases then extended this metric, one orthogonal radius-one vertex at a time: **8D** with 13 vertices and 78 pairs (DOI **10.5281/zenodo.24408344**); **9D** with 14 and 91 pairs (DOI **10.5281/zenodo.24408448**); **10D** with 15 and 105 (DOI **10.5281/zenodo.24408569**); **11D** with 16 and 120 (DOI **10.5281/zenodo.24408650**); **12D** with 17 and 136 (DOI **10.5281/zenodo.24408720**); and **13D** with 18 vertices and 153 pairs (DOI **10.5281/zenodo.24408769**).

This new 14D record is explicitly derived from **the frozen D13 GitHub source tag** `Topbrutus/polybrutus-d13@v0.1.0` at source commit `4d5f10de586e6677ddbe1d90b18218b46602d14e`. The old mathematical programs and 153-pair labelled metric are included without alteration in `prior/`. We do not modify the earlier canonical geometry, its previously published metrics or existing DOIs.

## 2. Exact nineteen-point metric

Let `R=1` temporarily. Write `p1,...,p18` for the frozen D13 exact vectors represented in fourteen coordinate-storage slots. The older five-simplex-vertex coordinate block lies in a four-dimensional centered hyperplane, giving one exact linear constraint within these slots.

Embed all predecessor vectors into fifteen storage-coordinate slots:

```
q_i=(p_i,0),       i=1,...,18.
```

Adjoin the nineteenth vector as the new orthogonal unit direction:

```
q19 = e15 = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,1).
```

Every vector has unit norm and the new vector is orthogonal to all prior vectors. Consequently, all **153 old squared distances are unchanged**, and for every predecessor index:

```
||q19 - q_i||² = ||q19||² + ||q_i||² - 2<q19,q_i>
              = 1+1-0 = 2.
```

For a general radius `R>0`, scale all coordinates by `R` and these new squared lengths become `2R²`. There are `C(19,2)=171` labelled unordered pairs, made up of 153 conserved pairs and eighteen new pairs.

For the normalized squared-distance family parameter `k=4d²/R²`, the complete exact histogram is:

| k | 4 | 7 | 8 | 9 | 10 | 12 | 13 | 16 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Number of pairs | 6 | 2 | **140** | 3 | 10 | 6 | 2 | 2 |

All eight counts sum to **171**. The exact sum of all squared pairwise distances is:

```
sum_{i<j} d_ij²/R² = 1415/4.
```

At radius one, the exact centroid in fifteen storage slots is

```
G=(0,0,1/38,0,0,0,0,0,1/19,1/19,1/19,1/19,1/19,1/19,1/19).
```

Fifteen storage slots should not be confused with **fifteen independent affine dimensions**: the centered simplex block introduces one exact linear relation.

## 3. Certified minimal affine dimension fourteen

Let `X` be the exact 19-by-15 matrix of stored point coordinates, let `D` be the 19-by-19 matrix of **squared labelled Euclidean distances**, and let `H=I-11ᵀ/19` be the centering matrix. The centered Euclidean distance Gram matrix is

```
B = -(1/2) H D H.
```

The first symbolic verifier checks three independent exact identities:

```
rank([q2-q1,...,q19-q1]) = 14;
rank(B) = 14;
B = (H X)(H X)^T.
```

The last equality proves positive semidefiniteness by an **exact algebraic factorization**, not by approximate floating-point eigenvalues. Because the full set of 171 labelled squared distances determines the centered Gram matrix uniquely, **every Euclidean realization of this same labelled metric has affine rank exactly fourteen**. This is the precise meaning of *Polybrutus 14D*.

A second verifier independently reconstructs the full metric from rational structural rules: the seven canonical vertices' exact rational coefficients of `sqrt(3)`, five simplex vertices whose interpoint squared distances are `5/2`, and seven perpendicular unit-axis points. The programs share the mathematical specification but not the generator implementation. All **171/171** labelled entries agree and their centered Gram matrices have the same exact rank.

## 4. An eightfold mode in a chosen weighted-graph model

For a mathematical comparison with earlier dimensional cases, assign a hypothetical scalar displacement and equal unit mass to each of the nineteen vertices. Define a **chosen ideal coupling model** by placing positive all-pairs graph weights `w_ij=R²/d_ij²`, with normalized weight scale one. The resulting weighted Laplacian `L14` is a model matrix, not a measured instrument.

The added nineteenth vertex connects to each of the eighteen old vertices with uniform weight `1/2`. For the preceding eighteen-vertex weighted Laplacian `L13`, we obtain the exact block form:

```
L14 = [ L13 + (1/2)I18      -(1/2)1 ]
      [ -(1/2)1ᵀ                  9  ].
```

Writing `chi18(z)=det(zI-L13)` and `chi19(z)=det(zI-L14)`, the uniform mode and intergroup mode decompose the new characteristic polynomial exactly as

```
chi19(z) = z(z-19/2) chi18(z-1/2)/(z-1/2).
```

The frozen 13D source previously established

```
chi18(z) = z(z-9)^7(z-17/2)^4 f6(z-11/2),
f6(z) = chiP7(z)/z,
```

where `chiP7` is the original canonical seven-vertex weighted graph's characteristic polynomial, and `f6` contains the six nonuniform graph modes. Substitution produces the exact new factorization

```
chi19(z) = z(z-19/2)^8(z-9)^4 f6(z-6).
```

The primary verifier computes the full **19-by-19 exact characteristic polynomial** independently and proves that it equals both the recurrence and closed form. It further proves `f6(7/2) != 0` and `f6(3) != 0`, ensuring there are no additional factors at the designated eigenvalues. Therefore the model exhibits **exact multiplicity eight at eigenvalue 19/2** and **exact multiplicity four at eigenvalue 9**.

The independent rational verifier reconstructs the complete graph Laplacian and calculates the characteristic polynomial separately. It verifies the exact root multiplicities via the vanishing pattern of the polynomial derivatives. These eigenvalues are **dimensionless graph-model quantities**; no measured frequency in hertz or new physical resonance follows from them.

## 5. Reproducibility, falsification and release evidence

The research archive contains `src/verify_d14.py`, `tests/independent_d14.py`, `results/certificate_d14.json` listing **all 171 exact squared labelled distances**, previous source programs and certificates in `prior/`, mathematical specification, proof, provenance, SHA-256 integrity index and GitHub Actions checks.

To reproduce the result:

```sh
python -m pip install sympy==1.14.0
python src/verify_d14.py
python tests/independent_d14.py
```

Both verifier programs must report PASS and an identical SHA-256 digest for the regenerated JSON certificate. Four negative controls explicitly detect (1) corruption of a squared distance, (2) a repeated new vertex that lowers rank, (3) a new point tilted toward the old geometry rather than orthogonal and (4) swapped labels that preserve the histogram but violate the labelled pair metric.

For archival publication, the ZIP source is built from the immutable GitHub scientific tag, and is accompanied by this PDF and the standalone JSON exact metric certificate. All three artifacts have verifiable file hashes in the release record.

## 6. Mathematical precedence and limits

Orthogonal extension of Euclidean configurations, Euclidean distance Gram matrices and uniform graph-vertex joins are established mathematical concepts. This note contributes one explicit, independently reproducible **particular 14D labelled-distance configuration and ideal graph spectrum** in the Polybrutus-X72 research lineage. It **does not claim a novel universal theorem**, a fundamental fourteen-dimensional spacetime, a new particle, an experiment or a measurement of an actual physical oscillator.

The general dimension-raising process is intentionally systematic. Every new case receives its own reproducible certificate, code archive and scientific limitation statement. Independent human peer review of this particular note has not yet occurred.

## 7. Author, AI disclosure and rights

**Research author and scientifically responsible investigator:** Gabriel St-Pierre, independent researcher. He established the original Polybrutus geometry, initiated the research program and authorized this dimension's investigation and publication.

**Generative AI disclosure:** OpenAI ChatGPT (Astra) substantially assisted with mathematical proof checking, source inspection, exact symbolic computations, separate rational metric verification programming, selected graph-spectral model, provenance audit, scientific drafting and publication preparation. The AI is **not listed as an author**. Independent human peer review remains pending.

**Licenses:** mathematical note and narrative material CC BY 4.0; source code MIT.

**Prior research records:** canonical Polybrutus geometry https://github.com/Topbrutus/polybrutus/blob/main/SPECIFICATION.md ; D07 https://doi.org/10.5281/zenodo.24407952 ; D08 https://doi.org/10.5281/zenodo.24408344 ; D09 https://doi.org/10.5281/zenodo.24408448 ; D10 https://doi.org/10.5281/zenodo.24408569 ; D11 https://doi.org/10.5281/zenodo.24408650 ; D12 https://doi.org/10.5281/zenodo.24408720 ; D13 https://doi.org/10.5281/zenodo.24408769 ; immutable predecessor source https://github.com/Topbrutus/polybrutus-d13/tree/v0.1.0 .

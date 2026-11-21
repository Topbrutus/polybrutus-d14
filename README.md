# POLYBRUTUS 14D — Exact labelled Euclidean metric and eightfold ideal graph mode

**Research author and scientific responsibility:** Gabriel St-Pierre (Topbrutus), independent researcher.  
**Publication status:** Exact computational mathematics case study; not independently human peer reviewed.  
**Generative AI disclosure:** OpenAI ChatGPT (Astra) substantially assisted geometry verification, independently implemented rational checker, graph-model calculations, writing and publication workflow. AI is not an author.

## Verified results for radius R=1

- **19 labelled vertices**, **171** pairwise squared distances, minimal affine embedding dimension exactly **14**.
- **153/153** old labelled distances preserved from immutable **Polybrutus D13 v0.1.0**.
- **18** new pair distances with squared value exactly **2**, from one additional unit vector orthogonal to all preceding vertices.
- Eight normalized squared-distance classes `k=4d²/R²`: `{4:6,7:2,8:140,9:3,10:10,12:6,13:2,16:2}`.
- Exact sum of pairwise squared distances: `1415 R²/4`.
- Exact direct affine difference rank=14 and centered squared-distance Gram rank=14; positive semidefinite factorization `B=(HX)(HX)^T`.
- **Chosen ideal graph model:** equal-mass scalar displacements and all-pair couplings `w_ij=R²/d²`; the weighted Laplacian has eigenvalue **19/2** with multiplicity exactly **8**, and eigenvalue **9** with multiplicity exactly **4**. Not an observed system.
- Two separately implemented checkers pass, including **171/171 labelled pairs**, the Gram ranks and both characteristic-polynomial multiplicities. Four intentionally invalid variants fail the intended tests.

## Reproduce exact verification

```sh
python -m pip install sympy==1.14.0
python src/verify_d14.py
python tests/independent_d14.py
```

The independently coded checker uses rational distance rules without importing the main point construction. `prior/` contains the exact frozen previous source chain, copied from `Topbrutus/polybrutus-d13@v0.1.0` at commit `4d5f10de586e6677ddbe1d90b18218b46602d14e`.

## Research files

- `src/verify_d14.py` — exact source, full Gram and graph spectrum, negative controls.
- `tests/independent_d14.py` — separate rational metric and characteristic-polynomial root multiplicity checks.
- `results/certificate_d14.json` — all 171 exact labelled squared distances, rank, spectrum and provenance.
- `SPECIFICATION_D14.md`, `PREUVE_D14.md`, `PROVENANCE.md` — exact specification, mathematical proof, source chain.
- `publication/POLYBRUTUS_14D_NOTE.pdf`, `.md` — unreviewed scientific note (CC BY 4.0).
- `SHA256SUMS.txt` — tag-source Git blob integrity index; code MIT.

## Source lineage

- Canonical Polybrutus seven-point specification: https://github.com/Topbrutus/polybrutus/blob/main/SPECIFICATION.md
- D07: https://doi.org/10.5281/zenodo.24407952
- D08: https://doi.org/10.5281/zenodo.24408344
- D09: https://doi.org/10.5281/zenodo.24408448
- D10: https://doi.org/10.5281/zenodo.24408569
- D11: https://doi.org/10.5281/zenodo.24408650
- D12: https://doi.org/10.5281/zenodo.24408720
- D13: https://doi.org/10.5281/zenodo.24408769

**Scientific limits:** Orthogonal point extension and uniform graph spectral shifts are established techniques. The contribution is one reproducible particular 14D metric and chosen graph model. No novel universal theorem, extra physical spacetime dimension or experimentally observed frequency is claimed.

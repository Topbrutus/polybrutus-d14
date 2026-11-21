# Polybrutus D14 — audited publication procedure

A reproducible, **unreviewed mathematical preprint** with 19 labelled points and exact affine dimension 14. No claims of physical new dimensions or a novel universal theorem.

1. Run the exact and independently implemented verification programs.
2. Create the **private** GitHub D14 repository, add CI and verify a successful GitHub Actions run.
3. Freeze exactly the successful science commit as tag `v0.1.0`.
4. Create source ZIP with `git archive v0.1.0`, not from a mutable directory. Record SHA-256 and sizes for source ZIP, PDF, and certificate JSON.
5. Create or reuse **one** Zenodo draft via the authorized direct REST API; verify author, DOI ancestry, CC BY 4.0 license, AI disclosure, frozen Git tag and exactly three attached file checksums.
6. Make GitHub public, verify tag using public GitHub API, publish the existing Zenodo draft and verify DOI and all three public files.
7. Link the DOI in README, CITATION.cff, release_manifest.json and central Memoria. Preserve the frozen source tag. Do not generate duplicates through automatic GitHub-to-Zenodo harvesting.

No private credentials or unrelated conversations appear in public source.

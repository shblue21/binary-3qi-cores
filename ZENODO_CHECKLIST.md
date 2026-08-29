# Zenodo release checklist

- [ ] Run make clean and make release-check.
- [ ] Visually inspect every rendered PDF page.
- [ ] Confirm all references and cross-references resolve.
- [ ] Confirm the finite verification programs pass twice.
- [ ] Review AI_DISCLOSURE.md.
- [ ] Confirm author name and email.
- [ ] Confirm title, abstract, keywords, and license in .zenodo.json.
- [ ] Reserve a new Zenodo DOI.
- [ ] Insert the reserved DOI into CITATION.cff, README, and PDF metadata.
- [ ] Tag the matching Git commit.
- [ ] Build a source archive from the tag.
- [ ] Generate SHA-256 and MD5 manifests.
- [ ] Upload the PDF and source archive.
- [ ] Verify Zenodo file hashes before publishing.
- [ ] Publish only after a final independent mathematical audit.

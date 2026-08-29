PYTHON ?= python3
PDFLATEX ?= pdflatex
BIBTEX ?= bibtex
OUTPDF := output/pdf/binary-3qi-cores-preprint.pdf
SOURCE_DATE_EPOCH ?= 1788048000
export SOURCE_DATE_EPOCH
export FORCE_SOURCE_DATE = 1

.PHONY: all paper check optimized-check reproducible-check package clean release-check

all: paper check

paper:
	mkdir -p output/pdf
	$(PDFLATEX) -interaction=nonstopmode -halt-on-error main.tex
	$(BIBTEX) main
	$(PDFLATEX) -interaction=nonstopmode -halt-on-error main.tex
	$(PDFLATEX) -interaction=nonstopmode -halt-on-error main.tex
	cp main.pdf $(OUTPDF)

check:
	$(PYTHON) supplementary/verify_certificates.py
	$(PYTHON) supplementary/verify_lift_small.py

optimized-check:
	$(PYTHON) -O supplementary/verify_certificates.py
	$(PYTHON) -O supplementary/verify_lift_small.py

reproducible-check: paper
	tmp_dir=$$(mktemp -d); \
	trap 'rm -rf "$$tmp_dir"' EXIT; \
	cp main.tex references.bib Makefile "$$tmp_dir"/; \
	mkdir -p "$$tmp_dir/supplementary"; \
	cp supplementary/verify_certificates.py supplementary/verify_lift_small.py \
	  "$$tmp_dir/supplementary"/; \
	$(MAKE) -C "$$tmp_dir" paper; \
	cmp $(OUTPDF) "$$tmp_dir/$(OUTPDF)"

release-check: all optimized-check reproducible-check
	pdfinfo $(OUTPDF)
	test -s $(OUTPDF)

package: release-check
	$(PYTHON) supplementary/build_release.py

clean:
	rm -f main.aux main.bbl main.blg main.log main.out main.pdf

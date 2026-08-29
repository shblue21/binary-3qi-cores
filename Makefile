PYTHON ?= python3
PDFLATEX ?= pdflatex
BIBTEX ?= bibtex
OUTPDF := output/pdf/binary-3qi-cores-preprint.pdf

.PHONY: all paper check clean release-check

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

release-check: all
	pdfinfo $(OUTPDF)
	test -s $(OUTPDF)

clean:
	rm -f main.aux main.bbl main.blg main.log main.out main.pdf

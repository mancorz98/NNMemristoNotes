# Main document name (without .tex extension)
MAIN = main_ieee

# Output directory
OUTDIR = build

.PHONY: all clean

all:
	latexmk -synctex=1 -interaction=nonstopmode -file-line-error -pdf -outdir=$(OUTDIR) $(MAIN).tex

clean:
	latexmk -C -outdir=$(OUTDIR)
	rm -f $(OUTDIR)/*.synctex.gz
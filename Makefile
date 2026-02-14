COMPILER = pdflatex
BIBTEX = bibtex
SOURCES = main_ieee.tex
OUTPUT = main_ieee.pdf

.PHONY:  clean

all: $(OUTPUT) clean
	echo "Build complete. Output file: $(OUTPUT)"

$(OUTPUT): $(SOURCES)
	$(COMPILER) $(SOURCES)
	$(BIBTEX) $(basename $(SOURCES))
	$(COMPILER) $(SOURCES)
	$(COMPILER) $(SOURCES)
	$( if [ -f $(OUTPUT) ]; then echo "Compilation successful: $(OUTPUT)"; else echo "Compilation failed."; exit 1; fi )

clean: $(OUTPUT)
	rm -f  *.aux *.bbl *.blg *.log *.toc *.out *fls 



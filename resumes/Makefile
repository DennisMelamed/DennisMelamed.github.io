SHELL=zsh
JSON_FILE := $(shell print -l -r -- json/*(n) | tail -1)
MOST_RECENT_PDF_FILE = $(shell print -l -r -- pdfs/*(n) | tail -1)

all: resume recent_update

recent_update:
	@cp $(MOST_RECENT_PDF_FILE) most_recent/ResumeDennisMelamed.pdf
	@git add most_recent/ResumeDennisMelamed.pdf $(MOST_RECENT_PDF_FILE) $(JSON_FILE)


resume: FORCE
	@echo "--------------------"
	@echo "[PDF]"
	@cd typst_resume && uv run src/typst_resume/gen_typst.py ../json/ ../pdfs ../typst #$(JSON_FILE) /tmp/intermediate ../pdfs
	@echo "done!"
	@echo "--------------------"


FORCE:

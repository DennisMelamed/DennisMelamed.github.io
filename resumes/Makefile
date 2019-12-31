SHELL=zsh
DOC_FILE := $(shell print -l -r -- docs/*(n) | tail -1)
MOST_RECENT_PDF_FILE = $(shell print -l -r -- pdfs/*(n) | tail -1)

all: resume recent_update

recent_update: resume
	@cp $(MOST_RECENT_PDF_FILE) most_recent/ResumeDennisMelamed.pdf
	@git add most_recent/ResumeDennisMelamed.pdf $(MOST_RECENT_PDF_FILE) $(DOC_FILE)


resume: FORCE
	@echo "--------------------"
	@echo $(DOC_FILE)
	@echo "[PDF]"
	@/Applications/LibreOffice.app/Contents/MacOS/soffice --headless --convert-to pdf $(DOC_FILE) --outdir pdfs/
	@echo "[TXT]"
	@/Applications/LibreOffice.app/Contents/MacOS/soffice --headless --convert-to txt $(DOC_FILE) --outdir txts/
	@echo "done!"
	@echo "--------------------"

full: all/resume.json FORCE
	@echo "--------------------"
	@echo "--------------------"
	
cv: cv/cv_filters.filter FORCE
	@echo "--------------------"
	@echo "--------------------"

FORCE:

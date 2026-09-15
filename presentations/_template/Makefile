# Generic Makefile for rpki_audit conference decks.
#
# File names are derived from the directory name so that copying this
# template to `presentations/<event>/` and renaming the two source files to
# `<event>_presentation.md` / `<event>-theme.css` is enough to build — no
# edits to this Makefile are required.
#
# If you don't want a custom theme, delete the *-theme.css file and remove
# THEME and every `--theme-set $(THEME)` below.

NAME    := $(notdir $(CURDIR))
SRC     := $(NAME)_presentation.md
THEME   := $(NAME)-theme.css
HTML    := $(NAME)_presentation.html
PDF     := $(NAME)_presentation.pdf

MARP      := npx @marp-team/marp-cli
MARPFLAGS := --allow-local-files --theme-set $(THEME)

# Set to the final slide count before running `make check`.
SLIDES  ?= 0

.PHONY: all html pdf check clean

all: html pdf

html: $(HTML)

$(HTML): $(SRC) $(THEME)
	$(MARP) $(MARPFLAGS) $< -o $@

pdf: $(PDF)

$(PDF): $(SRC) $(THEME)
	$(MARP) $(MARPFLAGS) --pdf --pdf-outlines $< -o $@

check:
	@python3 check_render.py $(HTML) $(PDF) $(SLIDES)

clean:
	rm -f $(HTML) $(PDF)

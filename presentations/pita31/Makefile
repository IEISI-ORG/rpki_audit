# Makefile for the PITA31 deck. Generated from presentations/_template/ —
# see that directory for the reusable version this was copied from.

NAME    := $(notdir $(CURDIR))
SRC     := $(NAME)_presentation.md
THEME   := $(NAME)-theme.css
HTML    := $(NAME)_presentation.html
PDF     := $(NAME)_presentation.pdf

MARP      := npx @marp-team/marp-cli
# --theme-set (array-type) must come before the bare --html flag, or this
# marp-cli's yargs parser misparses and silently fails to build the HTML.
MARPFLAGS := --allow-local-files --theme-set $(THEME) --html

# 32 slides as of the 2026-09-15 draft — update if the deck grows/shrinks.
SLIDES  ?= 32

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

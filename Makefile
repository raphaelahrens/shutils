
FILES = $(shell find . -maxdepth 1 -type f -name "[a-z]*" ! -name "Makefile")
USER = $(shell id --user --name)

.PHONY: all clean

all: $(FILES)
	echo "$(FILES)"

/home/$(USER)/%: ./%
	echo "$<"

clean:
	rm -r ~/bin/*

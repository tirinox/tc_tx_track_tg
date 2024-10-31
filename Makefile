default: help

.PHONY: help
help: # Show help for each of the Makefile recipes.
	@grep -E '^[a-zA-Z0-9 -_]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

.PHONY: docker_build
docker_build: # Built Docker image
	docker build -t tc-tx-track-tg-bot .

PWD := $(shell pwd)

.PHONY: docker_run
docker_run: # Run Docker image. Container is removed after stop. For development purposes
	echo $(PWD)
	docker run --rm -d --name tc-tx-track-tg-bot \
		-v $(PWD)/.env:/app/.env \
		-v $(PWD)/src/:/app/src \
		 tc-tx-track-tg-bot

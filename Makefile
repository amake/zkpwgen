env := .env

$(env):
	python3 -m venv $(@)
	$(env)/bin/pip install --upgrade pip build twine
	$(env)/bin/pip install -e .

.PHONY: test
test: ## Run tests
test: test-bin test-install

.PHONY: test-bin
test-bin: | $(env)
	$(env)/bin/zkpwgen --help
	$(env)/bin/zkpwgen

.PHONY: test-install
test-install:
	python3 -m venv $(env)-test
	$(env)-test/bin/pip install --no-deps zkpwgen
	$(env)-test/bin/zkpwgen --help
	rm -rf $(env)-test

.PHONY: clean
clean: ## Clean up build artifacts
	rm -rf dist $(env)-test

.PHONY: clobber
clobber: ## Remove all build artifacts and virtualenv
clobber: clean
	rm -rf $(env)

.PHONY: build
build: ## Build package
build: dist | $(env)

dist: | $(env)
	$(env)/bin/python3 -m build

.PHONY: publish
publish: ## Publish package to PyPI
publish: build | $(env)
	$(env)/bin/twine upload dist/*

.PHONY: help
help: ## Show this help text
	$(info usage: make [target])
	$(info )
	$(info Available targets:)
	@awk -F ':.*?## *' '/^[^\t].+?:.*?##/ \
         {printf "  %-24s %s\n", $$1, $$2}' $(MAKEFILE_LIST)


#
## Bloombox: Python API Client
#

ENV_PATH ?= .env
VERBOSE ?= no
VERSION ?= 0.0.1
SERVICES ?= checkin:v1beta1 devices:v1beta1 menu:v1beta1 shop:v1 telemetry:v1beta3
SERVICE_NAMES ?= $(foreach svc,$(SERVICES),$(firstword $(subst :, ,$(svc))))

TEST_FLAGS = --no-byte-compile \
		--traverse-namespace \
		--with-coverage \
		--cover-package=bloombox \
		--cover-branches \
		--cover-html --cover-html-dir=build/coverage-html \
		--cover-xml --cover-xml-file=build/coverage.xml \
		--with-xunit --xunit-file=build/tests.xml --xunit-testsuite-name=bloombox

ifeq ($(VERBOSE),yes)
CP_FLAGS ?= v
RM_FLAGS ?= v
TEST_FLAGS += -v
else
CP_FLAGS ?=
RM_FLAGS ?=
endif

PYTHON_BUILD_TARGETS ?= build build_py
PYTHON_DIST_TARGETS ?= sdist bdist bdist_dumb bdist_egg bdist_wheel
PYTHON_TARGETS ?= $(PYTHON_BUILD_TARGETS) $(PYTHON_DIST_TARGETS)
SCHEMA_PATH ?= src/bloombox/schema

all: env build

env: $(ENV_PATH)

clean-schema:
	@echo "Cleaning embedded schema..."
	@rm -fr$(RM_FLAGS) $(SCHEMA_PATH)/*
	@$(MAKE) -C schema clean

clean:
	@echo "Cleaning PYC files..."
	@find . -name '*.py[c,o]' -delete
	@echo "Cleaning build..."
	@rm -fr$(RM_FLAGS) build dist

distclean: clean clean-schema
	@echo "Cleaning environment..."
	@rm -fr$(RM_FLAGS) $(ENV_PATH)

$(ENV_PATH):
	@echo "Setting up environment..."
	@mkdir -p $(ENV_PATH)
	@virtualenv $(ENV_PATH)
	@$(ENV_PATH)/bin/pip install -r requirements.txt
	@echo "Environment ready."

submodules:
	@echo "Fetching submodules..."
	@git submodule update --init --recursive

update-schema: submodules
	@echo "Updating schema..."
	@git submodule update --init --remote

sync-schema: update-schema clean-schema embedded-schema
	@echo "Sync done."

schema/languages/python:
	@echo "Building schema..."
	@$(MAKE) -C schema LANGUAGES="python pygrpc"

$(SCHEMA_PATH)/__init__.py:
	@echo "Installing Schema..."
	@mkdir -p $(SCHEMA_PATH) $(SCHEMA_PATH)/services
	@cd schema/languages/python && cp -fr$(CP_FLAGS) ./* ../../../$(SCHEMA_PATH)/

$(SCHEMA_PATH)/services/descriptor.py:
	@echo "Installing services..."
	@for service in $(SERVICE_NAMES); do \
		echo "- Installing '$$service'..."; \
		mkdir -p $(SCHEMA_PATH)/services/$$service; \
		cp -fr$(CP_FLAGS) schema/languages/pygrpc/$$service/* $(SCHEMA_PATH)/services/$$service; done

embedded-schema: schema/languages/python $(SCHEMA_PATH)/__init__.py $(SCHEMA_PATH)/services/descriptor.py
	@echo "Fixing up modules..."
	@cd $(SCHEMA_PATH)/services && for directory in `find -s -x . -type d | xargs`; do touch $$directory/__init__.py; done
	@echo "Embedded schema ready."

build:
	@python setup.py $(PYTHON_TARGETS)

test:
	@echo "Running testsuite..."
	@$(ENV_PATH)/bin/nosetests $(TEST_FLAGS) bloombox_tests

interactive: all
	@cd src && ../$(ENV_PATH)/bin/python -B

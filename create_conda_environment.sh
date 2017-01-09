#!/bin/bash

# Build environment based on environment.yml
conda env create

# Activate python_module_quickstart environment
source activate python_module_quickstart

# Install local project interactively to allow pytest to work
pip install -e .

# Deactivate
source deactivate

[![PyPI version](https://badge.fury.io/py/black-cgx.svg)](https://badge.fury.io/py/black-cgx)
[![CI status](https://github.com/fork-tongue/black-cgx/workflows/CI/badge.svg)](https://github.com/fork-tongue/black-cgx/actions)
[![black](https://img.shields.io/badge/code%20style-black-black)](https://pypi.org/project/black/)

# Black-cgx

Format CGX files with black.


## Usage

```sh
# Install in your environment (for example with poetry)
poetry add -D black-cgx
# Show help for the tool
poetry run black-cgx -h
# By default, will format every cgx file in current folder (recursively)
poetry run black-cgx
# Just check if there would be any changes
poetry run black-cgx --check
# Format just a single file
poetry run black-cgx my-component.cgx
# Format a folder and file
poetry run black-cgx ../folder_with_cgx_files my-component.cgx
```

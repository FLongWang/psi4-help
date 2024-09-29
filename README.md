# Psi4-help Script

## Overview

Psi4-help is a Python script designed to help users explore and understand the keywords and options available in the Psi4 quantum chemistry software. The script reads a YAML file containing Psi4 keyword information and provides a user-friendly interface to view and search through the data.

## Features

- List all top-level keys in the Psi4 keyword YAML file.
- Show detailed information for a specific top-level key, including optional parameters and descriptions.
- Print all top-level keys and their detailed information.
- Print all top-level keys and their secondary keys without descriptions.

## Requirements

- Python 3.6 or higher
- PyYAML
- colorama

## Installation

   ```sh
   pip install psi4-help
   ```

or

1. **Clone the repository:**

   ```sh
   git clone https://github.com/FLongWang/psi4-help.git
   cd psi4-help
   ```
2. ```sh
   pip install .
   ```
## usage

Command-Line Interface
After installation, you can start psi4-help by running the following command:
   ```sh
   psi4-help
   ```
Upon starting `psi4-help`, you will be presented with an interactive command-line interface. Below are the available commands and their functionalities:
- **`help` or `?`**:
  - Display help information for all available commands.
  
- **`exit` or `e`**:
  - Exit the `psi4-help` command-line interface.

- **`mod` or `module` or `top`**:
  - List all top-level Psi4 keyword modules.

- **`all`**:
  - List all Psi4 keywords with brief information (without descriptions).

- **`show <module>`** or **`list <module>`**:
  - Display all keywords and their detailed information for the specified module.
  - Example: `show adc`
  
- **`show <module> d`** or **`list <module> d`**:
  - Display all keywords and their detailed information, including descriptions, for the specified module.
  - Example: `show adc d`

- **`tree`**:
  - Display the psi4 keyswords in a tree structure.
   
<div align="center">

# What's HackMyCLI
HackMyCLI is a command line interface to manage the hackmyvm platform.<br>
It's created in Python and uses [python-fire](https://github.com/google/python-fire) for generating the interface.

</div>

---

# 🏁 Getting started

## Installation

### Using source code
```bash
# Clone repository and change directory to it
$ git clone https://github.com/tory1103/hackmycli.git
$ cd hackmycli

# Install dependencies
$ python3 -m pip install requirements.txt

# Change dir to source
$ cd src/hackmycli

# Run python3 script
$ python3 main.py <args>
```

### Using python3 setup
```bash
# Clone repository and change directory to it
$ git clone https://github.com/tory1103/hackmycli.git
$ cd hackmycli

# Install using setup.py
$ python3 setup.py install

# HackMyCLI is ready to use. Type: hack --help
$ hack --help
```
---

## 🎈 Documentation

### Configuring credentials with config
```bash
# Fresh configuration
# User and password would not be needed in future versions
$ hack config fresh <username> <password> <api_key>

# Skipping username and password
$ hack config key <api_key>
```

### Basic usage
```bash
# Main program syntax
$ hack <command> <parameters>

# Listing all avaliable machines
$ hack list all --update --descendant

# Downloading machine by name
$ hack download <machine_name>

# Downloading machine by URL
# URL must be google drive link for the moment
$ hack download <machine_URL> --no-verify

# Using config command
$ hack config fresh <username> <password> <api_key>

# Using config to add custom data
$ hack config add <key> <value>

# Using config to remove data
$ hack config remove <key>

# For more information about any command
# type: hack <command> --help
# All commands are not avaliable for the moment,
# HackMyVM API is under development
$ hack <command> --help
```

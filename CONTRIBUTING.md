# Contributing
Thank you from taking time and interest into contribution to our project.

Contribution is welcome and this document is here to help you out with getting ready in less than 5 minutes.

The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, 
and “OPTIONAL” in this document are to be interpreted as described in [RFC 2119](https://www.ietf.org/rfc/rfc2119.txt).


## How to contribute

You can contribute either by:
 - reporting bugs
 - requesting new features
 - suggesting changes
 - contributing to code

## Contributing to code
### Installation/Setup
Opyapi uses [poetry dependency manager](https://github.com/sdispater/poetry). 

Use poetry install to setup the project:
```bash
poetry install
``` 

Once project is installed you should be able to run tests:

```bash
poetry shell
pytest tests
```

### Submitting your code

Make sure your code is compatible with [PEP 8 standard](https://www.python.org/dev/peps/pep-0008/),
the easiest and the best way to assure the above is true is to run `black` before submitting your code:

```bash
poetry shell
black .
``` 

Please also make sure you follow the code guide.

### Code guide

#### Overview
This guide extends and expands on [PEP 8](https://www.python.org/dev/peps/pep-0008/), the basic coding standard. 

The style rules used here are to keep project's code clean and easy to maintain.

#### General

 - Submitted code **MUST** be compatible with python version >= 3.6
 - Abbreviations **MUST NOT** be used, they can lead to misunderstanding and bugs

#### Modules and imports

 - It is **REQUIRED** each function, class are fully annotated and types **MUST** be as explicit as possible
 - It is **RECOMMENDED** to use `typing` library to annotate codebase
 - Imports statements **MUST** be sorted alphabetically   
 - Relative imports **MUST** be defined below global imports
 - Each module **SHOULD** contain only one class or one function definition
 - Module name **SHOULD** reflect contained class or function name
 - If module contains more than one declaration, `__all__` keyword is **REQUIRED** at the end of the module
 - Newly created package **MUST** define `__init__` module

#### Tests
 - 

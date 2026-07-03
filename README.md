# ALX Higher Level Programming

Python projects built as part of the [ALX Software Engineering](https://www.alxafrica.com/) curriculum, progressing from basic syntax through object-oriented programming, unit testing, and a full Python/C hybrid OOP project. Each directory is a standalone module named for the concept it covers.

## About

This repository tracks my work through the "Higher Level Programming" track of ALX-SE, where Python is the primary language. The projects build on each other: early modules cover syntax, control flow, and data structures, while later ones move into classes, inheritance, exceptions, test-driven development, and serialization — culminating in the Almost a Circle project, which combines OOP design with a matching C-based unit test/checker suite.

## Repository structure

| Directory | Topic |
|---|---|
| [0x00-python-hello_world](./0x00-python-hello_world) | Python — Hello, World |
| [0x01-python-if_else_loops_functions](./0x01-python-if_else_loops_functions) | Python — if/else, loops, functions |
| [0x02-python-import_modules](./0x02-python-import_modules) | Python — import & modules |
| [0x03-python-data_structures](./0x03-python-data_structures) | Python — Data structures: Lists, Tuples |
| [0x04-python-more_data_structures](./0x04-python-more_data_structures) | Python — More data structures: Set, Dictionary |
| [0x05-python-exceptions](./0x05-python-exceptions) | Python — Exceptions |
| [0x06-python-classes](./0x06-python-classes) | Python — Classes and objects |
| [0x07-python-test_driven_development](./0x07-python-test_driven_development) | Python — Test-driven development (unittest, doctest) |
| [0x08-python-more_classes](./0x08-python-more_classes) | Python — More classes and objects |
| [0x09-python-everything_is_object](./0x09-python-everything_is_object) | Python — Everything is object |
| [0x0A-python-inheritance](./0x0A-python-inheritance) | Python — Inheritance |
| [0x0B-python-input_output](./0x0B-python-input_output) | Python — Input/Output (file I/O, JSON, pickling) |
| [0x0C-python-almost_a_circle](./0x0C-python-almost_a_circle) | Python — Almost a Circle (OOP capstone: `Base`, `Rectangle`, `Square`, with full unittest coverage and a C-based checker) |

Each directory holds the individual task scripts for that topic, plus any accompanying `README.md`, `tests/`, or `models/` subfolders where relevant (notably in `0x0C`).

## Requirements

- **Python 3** (all scripts start with `#!/usr/bin/python3`)
- Code follows [pycodestyle](https://pypi.org/project/pycodestyle/) (PEP 8) style
- Every module, class, and function is documented
- `0x0C-python-almost_a_circle` additionally uses **unittest** for Python test coverage and includes a small **C** component for its checker/test suite

## Usage

Clone the repository and run any script directly with Python 3:

```bash
git clone https://github.com/Anthony4pf/alx-higher_level_programming.git
cd alx-higher_level_programming/0x00-python-hello_world
python3 0-*.py
```

For the Almost a Circle project, run the unit tests with:

```bash
cd 0x0C-python-almost_a_circle
python3 -m unittest discover tests
```

## Author

**Anthony** ([@Anthony4pf](https://github.com/Anthony4pf))

## Acknowledgments

Projects and task specifications from the [ALX Software Engineering](https://www.alxafrica.com/) program.

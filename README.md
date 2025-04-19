# 🍪 Cookiecutter Python Template 🐍

[![CI](https://github.com/mohammadraziei/cookiecutter-python-template/actions/workflows/test.yml/badge.svg)](https://github.com/mohammadraziei/cookiecutter-python-template/actions/workflows/test.yml)
![build](https://img.shields.io/badge/build-hatch-blue)
![lint](https://img.shields.io/badge/lint-ruff-blue)
![test](https://img.shields.io/badge/test-pytest--cov-blue)

A modern, opinionated Cookiecutter template for quickly bootstrapping clean, production-ready Python projects.

---

## ❓ What is this?

This repository provides a Cookiecutter template designed to automate the creation of Python project scaffolding. It helps you start new Python projects with best practices in mind, including:

- 📁 Standardized folder structure
- 🧪 Automated test setup
- 🧹 Linting and formatting configuration
- 📦 Dependency management
- 🏷️ Versioning and packaging setup

With this template, you can focus on writing code instead of spending time on repetitive setup tasks.

---

## 🛠️ Technologies Used

This template leverages the following tools and technologies:

- 🍪 **[Cookiecutter](https://cookiecutter.readthedocs.io/):** For project templating and scaffolding.
- 🚀 **[Hatch](https://hatch.pypa.io/):** For modern Python packaging, environment management, and versioning.
- ✅ **[pytest](https://docs.pytest.org/):** For testing your code.
- 📊 **[coverage](https://coverage.readthedocs.io/):** For measuring code coverage.
- 🎨 **[black](https://black.readthedocs.io/):** For automatic code formatting.
- ⚡ **[ruff](https://docs.astral.sh/ruff/):** For fast linting and code quality checks.
- 🔎 **[mypy](https://mypy-lang.org/):** For static type checking.

All configurations are pre-set, so you get a clean, maintainable, and production-ready Python project out of the box.

---

## 🚀 How to Use

To generate a new Python project using this template, run:

```sh
python -m cookiecutter gh:mohammadraziei/cookiecutter-python-template
```

You will be prompted for project-specific information (name, description, author, etc.), and a new project directory will be created with all the necessary files and structure.

---

## ⚙️ Prerequisites

Before you start, make sure you have the following installed:

- 🐍 **Python 3.7 or higher**  
  Download from [python.org](https://www.python.org/downloads/)

- 🍪 **Cookiecutter**  
  Install via pip:
  ```bash
  pip install cookiecutter
  ```

- 🚀 **Hatch** (for development, testing, and linting)  
  Install via pip:
  ```bash
  pip install hatch
  ```

- 🧪 **pytest** and **pytest-cov** (for running tests and coverage)  
  Install via pip (if you want to run tests directly, outside Hatch):
  ```bash
  pip install pytest pytest-cov
  ```

- 🧹 **ruff** (for linting and formatting)  
  Install via pip (if you want to run linting directly, outside Hatch):
  ```bash
  pip install ruff
  ```

> 💡 If you use Hatch (recommended), it will automatically manage these dependencies for you in isolated environments.

---

## 🧪 Running Tests, Coverage & Linting

After generating your project, you can use the following commands to ensure code quality and correctness:

### 🧪 Run Tests

```bash
python -m pytest
```
or

```bash
hatch run test
```
Runs all tests using **pytest**.

### 📊 Run Tests with Coverage

```bash
python -m pytest --cov
```
or

```bash
hatch run cov
```
Runs tests and generates a coverage report.

To generate an HTML coverage report (viewable in your browser):

```bash
python -m pytest --cov --cov-report=term --cov-report=html
```
or

```bash
hatch run cov
coverage html
```
### 🧹 Run Linter & Formatter

```bash
python -m ruff check .
```
or

```bash
hatch run lint:all
```
Checks code style and type hints using **ruff**, **black**, and **mypy**.

### 🎨 Auto-format Code

```bash
python -m ruff check --fix .
```
or

```bash
hatch run lint:fmt
```
Automatically formats your code and fixes lint issues.

---

## ✨ Features

- 🤖 Automated setup for testing, linting, and formatting
- 📝 Pre-configured `pyproject.toml` for modern Python workflows
- 🐍 Support for multiple Python versions (3.7+)
- 🧪 Clean separation of source code and tests
- ⚙️ Ready-to-use scripts for common development tasks

---

## 🗂️ Folder Structure

A typical generated project will look like:

```
my-project/
├── src/
│   └── my_package/
│       ├── __init__.py
│       ├── __about__.py
│       ├── core.py
│       └── utils.py
├── tests/
│   └── test_example.py
├── pyproject.toml
├── README.md
├── .gitignore
└── requirements.txt
```

---

## 💡 Why Use This Template?

- ⏱️ **Saves time:** Automates repetitive setup tasks.
- 🏆 **Best practices:** Enforces modern Python standards.
- 🧩 **Consistency:** Ensures all your projects start with the same high-quality foundation.

---

Feel free to contribute or open issues if you have suggestions or encounter problems! 🚀✨

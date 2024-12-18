# Playwright-Python-BDD

This repository contains a test automation framework built using **Playwright**, **Pytest-BDD**, and **Python**. It supports both headless and headed browser testing with HTML reporting.

## Prerequisites

1. **Install Python** (version 3.12 or above)
   - https://www.python.org/downloads/

2. **Install Node.js** (for Playwright dependencies)
   - https://nodejs.org/

3. **Install pip** (Python's package manager)
   - Python usually includes pip by default. Verify by running:
     ```bash
     python -m pip --version
     ```
4. **Install packages**
   - pip install -r requirements.txt
   - python -m playwright install --with-deps

## Getting Started

Create and activate a virtual environment to isolate dependencies ( for Windows)
```bash
python -m venv venv
.\venv\Scripts\activate
```
Follow the steps below to run tests:

### 1. Clone the Repository

```bash

git clone https://github.com/Dzanan91/playwright-python-bdd.git
cd playwright-python-bdd

Run All Tests
To execute all tests in the suite and create HTML report

pytest --gherkin-terminal-reporter --log-cli-level=INFO --html=reports/report.html --self-contained-html

Run a Specific Test
To run a specific test (e.g., a test with marker T1):

pytest -m T1 --gherkin-terminal-reporter --log-cli-level=INFO --html=reports/report.html --self-contained-html


# SauceDemo Playwright Python Automation Framework

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Playwright](https://img.shields.io/badge/Playwright-Automation-green)
![Pytest](https://img.shields.io/badge/Pytest-Testing-orange)
![GitHub Actions](https://img.shields.io/badge/CI-GitHub_Actions-black)

## Project Overview

This project implements a scalable UI automation
framework for the SauceDemo e-commerce application.

The framework is developed using Python, Playwright,
Pytest, and Page Object Model.

## Application URL

https://www.saucedemo.com/

## Tech Stack

- Python
- Playwright
- Pytest
- Page Object Model
- Pytest HTML
- Faker
- Git
- GitHub Actions

## Features

- Page Object Model architecture
- Reusable page methods
- Pytest fixtures
- Data-driven testing
- Positive and negative scenarios
- Dynamic test data
- Logging
- Failure screenshots
- HTML reporting
- Parallel execution
- GitHub Actions CI/CD

## Project Structure

- config: Application configuration
- pages: Page Object Model classes
- tests: Automation test scripts
- utils: Reusable utilities
- test_data: External test data
- reports: Execution reports
- screenshots: Failure screenshots
- logs: Execution logs
- .github/workflows: CI/CD configuration

## Installation

Clone the repository:

```bash
git clone https://github.com/Geeta-Metri-904/playwright-python-ecommerce-automation.git
```

Navigate to the project:

```bash
cd saucedemo-playwright-python
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install browser:

```bash
playwright install chromium
```

## Execution

Run all tests:

```bash
pytest
```

Run smoke tests:

```bash
pytest -m smoke
```

Run regression tests:

```bash
pytest -m regression
```

Run login tests:

```bash
pytest -m login
```

Run tests in parallel:

```bash
pytest -n 2
```

Run tests with headed browser:

```bash
pytest --headed
```

## Reporting

HTML reports are generated at:

reports/report.html

## CI/CD

GitHub Actions automatically executes the
automation tests on pushes and pull requests.

Execution reports and failure screenshots
are uploaded as workflow artifacts.

## Test Scenarios

### Login
- Valid login
- Invalid login
- Locked user
- Empty credentials

### Inventory
- Product listing
- Product sorting
- Add product

### Cart
- Add product
- Remove product
- Multiple products

### Checkout
- Checkout validation
- Order overview
- Successful order placement

### Navigation
- Logout

## Author

Geeta Metri ( QA Automation Engineer )

## License

This project is intended for learning and
automation testing practice.

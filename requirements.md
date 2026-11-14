
# SauceDemo Playwright Python Automation Framework

## 1. Project Overview

Project Name:
SauceDemo Web Application Automation

Project Type:
Web UI Automation Testing

Automation Tool:
Playwright

Programming Language:
Python

Test Framework:
Pytest

Design Pattern:
Page Object Model (POM)

CI/CD:
GitHub Actions

Reporting:
Pytest HTML Report

Application:
https://www.saucedemo.com/

## 2. Project Objective

The objective of this project is to automate the
functional testing of the SauceDemo e-commerce
application using Playwright with Python.

The framework should provide reusable, scalable,
maintainable, and reliable automation scripts.

## 3. Functional Requirements

### 3.1 Login Module

- Verify successful login with valid credentials.
- Verify login with invalid username.
- Verify login with invalid password.
- Verify locked-out user functionality.
- Verify login with empty username.
- Verify login with empty password.
- Verify error messages.

### 3.2 Inventory Module

- Verify inventory page loading.
- Verify all products are displayed.
- Verify product names.
- Verify product prices.
- Verify product sorting.
- Verify add-to-cart functionality.

### 3.3 Shopping Cart Module

- Verify cart navigation.
- Verify added products.
- Verify cart badge count.
- Verify multiple products in cart.
- Verify product removal.
- Verify empty cart functionality.

### 3.4 Checkout Module

- Verify checkout navigation.
- Verify first name field.
- Verify last name field.
- Verify postal code field.
- Verify mandatory field validation.
- Verify checkout overview.
- Verify product information.
- Verify successful order placement.
- Verify order confirmation message.

### 3.5 Navigation Module

- Verify menu functionality.
- Verify logout.
- Verify return to inventory page.
- Verify application navigation.

## 4. Non-Functional Requirements

- Framework should be maintainable.
- Framework should support reusable components.
- Framework should support parallel execution.
- Framework should support browser selection.
- Framework should support headless execution.
- Framework should support execution logs.
- Framework should capture failure screenshots.
- Framework should generate HTML reports.
- Framework should support CI/CD execution.

## 5. Technical Requirements

### Software

- Python 3.11 or later
- Playwright
- Pytest
- Pytest-Playwright
- Pytest-HTML
- Pytest-xdist
- Python-dotenv
- Faker
- Git
- GitHub
- Visual Studio Code

### Browser

- Chromium
- Firefox
- WebKit

### Operating Systems

- Windows
- Linux
- macOS

## 6. Framework Architecture

### Page Object Model

Each application page should have an individual
Python class.

Examples:
- LoginPage
- InventoryPage
- CartPage
- CheckoutPage

### Test Layer

Test scripts should contain test scenarios and
business validation.

### Utility Layer

Common reusable methods should be maintained in
the utils package.

Examples:
- Logging
- Assertions
- Dynamic test data
- Screenshot helpers

### Configuration Layer

Application URL, browser configuration, timeout,
and environment variables should be centrally
managed.

## 7. Test Execution Requirements

Execute all test cases:

pytest

Execute smoke tests:

pytest -m smoke

Execute regression tests:

pytest -m regression

Execute login tests:

pytest -m login

Execute checkout tests:

pytest -m checkout

Execute tests in parallel:

pytest -n 2

Execute in Chromium:

pytest --browser chromium

Execute in Firefox:

pytest --browser firefox

Execute in WebKit:

pytest --browser webkit

Execute in headless mode:

pytest --headed=false

Execute in headed mode:

pytest --headed

## 8. Reporting Requirements

- Generate HTML execution reports.
- Display passed test cases.
- Display failed test cases.
- Display skipped test cases.
- Capture screenshots for failed tests.
- Maintain execution logs.
- Upload reports to GitHub Actions artifacts.

## 9. CI/CD Requirements

GitHub Actions should execute automation scripts
when code is pushed to the main or master branch.

The workflow should:

1. Checkout the repository.
2. Configure Python.
3. Install dependencies.
4. Install Playwright browsers.
5. Execute automation scripts.
6. Generate reports.
7. Upload test artifacts.

## 10. Acceptance Criteria

- Valid user should successfully log in.
- Locked-out user should not log in.
- Products should be displayed correctly.
- Users should be able to add products to cart.
- Users should be able to remove products.
- Checkout validation should work correctly.
- Successful orders should display confirmation.
- Failed tests should capture screenshots.
- HTML reports should be generated.
- GitHub Actions should execute the tests.

## 11. Future Enhancements

- API automation using Requests.
- Database validation.
- Cross-browser testing.
- Docker integration.
- Allure reporting.
- Retry mechanism.
- Test data management.
- Environment-based execution.
- Parallel execution optimization.
- Slack or email notifications.

## 12. Project Deliverables

- Automation framework source code.
- Page Object Model implementation.
- Pytest test cases.
- Reusable utility methods.
- Test data files.
- Execution logs.
- HTML reports.
- GitHub repository.
- GitHub Actions workflow.

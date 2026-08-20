# Playwright With Python Human Resource Management Test Automation Project
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-Automation-green.svg)](https://playwright.dev/python/)
[![Framework](https://img.shields.io/badge/Design%20Pattern-Page%20Object%20Model-orange.svg)]()

An automated end-to-end regression testing framework built with **Python**, **Playwright**, **Pytest**, and the Page Object Model (POM) design pattern to validate key OrangeHRM enterprise workflows including authentication, employee management (PIM), and dashboard operations.

---

## Key Architecture & Features

* **Page Object Model (POM):** Clean separation between element locators, page actions, and test assertions for scalable maintenance.
* **CI/CD Pipeline:** Automated build execution via GitHub Actions on every push and pull request.
* **Fixture Management:** Centralized browser lifecycle and setup/teardown handling via conftest.py.
* **Centralized Configuration:** Configurable environment settings and test parameters inside config.py.
* **Reporting:** Execution summaries, failure logs, and reports exported directly to `reports/`.

---

## Project Structure

```text
ORANGEHRM-PROJECT/
│
├── pages/                  # Page Object Model classes (Locators & Actions)
│   ├── login_page.py       # Page objects for user authentication workflows
│   ├── dashboard_page.py   # Page objects for dashboard navigation & widgets
│   └── pim_page.py         # Page objects for Employee Management (PIM)
│
├── reports/                # Test execution reports, failure screenshots, & logs
│
├── tests/                  # Test suites and execution scripts
│   ├── test_login.py       # Test cases for authentication & access control
│   ├── test_pim.py         # Test cases for adding, editing, and searching employees
│   └── test_dashboard.py   # Verification for dashboard layout and shortcuts
│
├── config.py               # Global configurations, credentials, & base URLs
├── conftest.py             # Pytest fixtures, driver management, and report hooks

```


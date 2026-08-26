from playwright.sync_api import sync_playwright
import pytest
from pages.login_page import LoginPage
import os


@pytest.fixture(scope='session')
def browser():
    with sync_playwright() as p:
        p.selectors.set_test_id_attribute("id")
        browser = p.chromium.launch(headless= False, slow_mo=1000)
        yield browser
        browser.close()


@pytest.fixture
def logged_in_page(page):
    login_page = LoginPage(page)

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page.login(
        os.getenv("USERNAME"),
        os.getenv("PASSWORD")
    )
    return page

@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()
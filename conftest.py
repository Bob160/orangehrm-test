from playwright.sync_api import sync_playwright
import pytest


@pytest.fixture(scope='session')
def browser():
    with sync_playwright() as p:
        p.selectors.set_test_id_attribute("id")
        browser = p.chromium.launch(headless= False, slow_mo=1000)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()
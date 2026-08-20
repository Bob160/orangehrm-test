from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from config import Config

import os

def test_login(page : Page) -> None:

    # page.goto(Config.BASE_URL)

    # login_page = LoginPage(page)

    # login_page.login(Config.USERNAME, Config.PASSWORD)

    response = page.goto(
        Config.BASE_URL,
        wait_until="domcontentloaded",
        timeout=60000
    )

    print(f"Status: {response.status if response else 'No response'}")
    print(f"URL: {page.url}")

    login_page = LoginPage(page)
    login_page.login(Config.USERNAME, Config.PASSWORD)

    #assert page.url == ("https://parabank.parasoft.com/parabank/register.htm")

    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
import re
from playwright.sync_api import Page, expect



class LoginPage:

    def __init__(self, page : Page):
        self.page = page

        self.username_input = page.locator("input[name=\"username\"]")
        self.password_input = page.locator("input[name=\"password\"]")
        self.login_button = page.get_by_role("button", name="Login")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.add_user_page import Add_user
from config import Config
from conftest import logged_in_page

def test_add_user(logged_in_page) -> None:

    new_user = Add_user(logged_in_page)


    new_user.add_user()
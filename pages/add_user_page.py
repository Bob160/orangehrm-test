import re 
from playwright.sync_api import Page, expect

class Add_user:

    def __init__(self, page : Page):

        self.page = page


        self.pim_menu_item = page.get_by_role("link", name="PIM")
        self.add_user_button = page.get_by_role("button", name=" Add")
        self.add_firstname = page.get_by_role("textbox", name="First Name")
        self.add_middlename = page.get_by_role("textbox", name="Middle Name")
        self.add_lastname = page.get_by_role("textbox", name="Last Name")
        self.add_employee_id = page.get_by_role("textbox").nth(4)
        self.create_login = page.locator(".oxd-switch-input")
        self.add_username = page.get_by_role("textbox").nth(5)
        self.add_password = page.locator("input[type=\"password\"]").first
        self.add_confirm_password = page.locator("input[type=\"password\"]").first
        self.save_user = page.get_by_role("button", name="Save")


    def add_user(self):
        self.pim_menu_item.click()
        self.add_user_button.click()
        self.add_firstname.fill("James")
        self.add_middlename.fill("John")
        self.add_lastname.fill("Dauda")
        self.add_employee_id.fill("0620")
        self.create_login.click()
        self.add_username.fill("Jboku")
        self.add_password.fill("@jboku380")
        self.add_confirm_password.fill("@jboku380")
        self.save_user.click()

        
        expect(self.page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/620")
   
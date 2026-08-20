import re
from playwright.sync_api import Page, expect

class RegisterPage:

    def __init__(self, page : Page):
        self.page = page

        self.register_firstname = page.get_by_test_id("customer.firstName")
        self.register_lastname = page.get_by_test_id("customer.lastName")
        self.register_address = page.get_by_test_id("customer.address.street")
        self.register_city = page.get_by_test_id("customer.address.city")
        self.register_state = page.get_by_test_id("customer.address.state")
        self.register_zip = page.get_by_test_id("customer.address.zipCode")
        self.register_phone = page.get_by_test_id("customer.phoneNumber")
        self.register_ssn = page.get_by_test_id("customer.ssn")
        self.register_username = page.get_by_test_id("customer-username")
        self.register_password = page.get_by_test_id("customer.password")
        self.register_confirmpassword = page.get_by_test_id("repeatedPassword")

        self.register_registerbutton = page.get_by_test_id("submit")


    def register(self,register_firstname, register_lastname, register_address, register_city, register_state, register_zip, register_phone, register_ssn, register_username, register_password, register_confirmpassword):
            self.register_firstname.fill(firstname)
            self.register_lastname.fill(lastname)
            self.register_address.fill(address)
            self.register_city.fill(city)
            self.register_state.fill(state)
            self.register_zip.fill(zipcode)
            self.register_phone.fill(phone)
            self.register_ssn.fill(ssn)
            self.register_username.fill(username)
            self.register_password.fill(password)
            self.register_confirmpassword.fill(repeatpassword)

            self.register_registerbutton.click()



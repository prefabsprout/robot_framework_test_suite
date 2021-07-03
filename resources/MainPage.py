from PageObjectLibrary import PageObject
from robot.api.deco import keyword


class MainPage(PageObject):
    PAGE_URL = ""

    _locators = {
        "profile_menu_button":  "css:.uui-profile-menu",
        "username": "css:#name",
        "password": "css:#password",
        "login_button": "css:#login-button",
        "service_dropdown_button": "css:.uui-header .nav > li:nth-child(3) > a",
        "different_element_page_button": "css:.uui-header .nav > li:nth-child(3) > ul > :nth-child(8)",
        "user_table_page_button": "css:.uui-header .nav > li:nth-child(3) > ul > :nth-child(6)"
    }

    def _is_current_page(self):
        location = self.selib.get_location()
        if not location.endswith(self.PAGE_URL):
            message = "Expected location to end with " + \
                      self.PAGE_URL + " but it did not"
            raise Exception(message)
        return True

    @keyword("I login as user")
    def login(self, username, password):
        self.selib.find_element(self.locator.profile_menu_button).click()
        self.selib.input_text(self.locator.username, username)
        self.selib.input_text(self.locator.password, password)
        self.selib.find_element(self.locator.login_button).click()

    @keyword("I click on Service button in Header")
    def open_service_sidebar_menu(self):
        self.selib.find_element(self.locator.service_dropdown_button).click()

    @keyword(name="I click on Different Elements button in Service dropdown")
    def go_to_different_elements_page(self):
        self.selib.find_element(self.locator.different_element_page_button).click()

    @keyword(name=" I click on User Table button in Service dropdown")
    def go_to_user_table_page(self):
        self.selib.find_element(self.locator.user_table_page_button).click()

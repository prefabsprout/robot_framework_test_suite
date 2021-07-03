from PageObjectLibrary import PageObject
from datetime import datetime

from robot.api.deco import keyword


class UserTablePage(PageObject):
    PAGE_URL = "/jdi-light/user-table.html"

    _locators = {
        "sergey_ivan_vip_checkbox": "css:#ivan",
        "log_section": "xpath://ul[@class='panel-body-list logs']//li[1]",
    }

    def _is_current_page(self):
        location = self.selib.get_location()
        if not location.endswith(self.PAGE_URL):
            message = "Expected location to end with " + \
                      self.PAGE_URL + " but it did not"
            raise Exception(message)
        return True

    @keyword("I select 'vip' checkbox for Sergey Ivan")
    def select_ivan_vip_checkbox(self):
        self.selib.find_element(self.locator.sergey_ivan_vip_checkbox).click()

    @keyword("I should see logs about interaction with VIP checkbox")
    def should_logs_about_vip_checkbox_interaction_exist(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        assert self.selib.find_element(
            self.locator.log_section).text == f'{current_time} Vip: condition changed to true'
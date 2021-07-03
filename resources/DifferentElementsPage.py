from PageObjectLibrary import PageObject
from datetime import datetime

from robot.api.deco import keyword


class DifferentElementsPage(PageObject):
    PAGE_URL = "/jdi-light/different-elements.html"

    _locators = {
        "wind_checkbox": "css:.main-content-hg > div:nth-child(2) >label:nth-child(3) input",
        "water_checkbox": "css:.main-content-hg > div:nth-child(2) >label:nth-child(1) input",
        "log_section": "xpath://ul[@class='panel-body-list logs']//li[1]"
    }

    def _is_current_page(self):
        location = self.selib.get_location()
        if not location.endswith(self.PAGE_URL):
            message = "Expected location to end with " + \
                      self.PAGE_URL + " but it did not"
            raise Exception(message)
        return True

    @keyword("I select Wind checkbox")
    def select_wind_checkbox(self):
        self.selib.find_element(self.locator.wind_checkbox).click()

    @keyword("I select Water checkbox")
    def select_water_checkbox(self):
        self.selib.find_element(self.locator.water_checkbox).click()

    @keyword("I should see logs about interaction with checkbox")
    def should_logs_about_checkbox_interaction_exist(self, checkbox_name):
        current_time = datetime.now().strftime("%H:%M:%S")
        assert self.selib.find_element(
            self.locator.log_section).text == f'{current_time} {checkbox_name}: condition changed to true'

from PageObjectLibrary import PageObject
from datetime import datetime

from robot.api.deco import keyword

import pandas as pd


class UserTablePage(PageObject):
    PAGE_URL = "/jdi-light/user-table.html"

    _locators = {
        "sergey_ivan_vip_checkbox": "css:#ivan",
        "log_section": "xpath://ul[@class='panel-body-list logs']//li[1]",
        "table": "xpath://table",
        "vip_checkboxes": "css:[type='checkbox']"
    }

    __test_data = {'Number': [1, 2, 3, 4, 5, 6],
                   'User': ["Roman", "Sergey Ivan", "Vladzimir", "Helen Bennett", "Yoshi Tannamuri", "Giovanni Rovelli"],
                   "Description": ["Wolverine", "Spider Man", "Punisher", "Captain America some description",
                                   "Cyclope some description", "Hulksome description"]}
    __test_dataframe = pd.DataFrame(data=__test_data)

    def _is_current_page(self):
        location = self.selib.get_location()
        if not location.endswith(self.PAGE_URL):
            message = "Expected location to end with " + \
                      self.PAGE_URL + " but it did not"
            raise Exception(message)
        return True

    def get_page_table_data(self):
        html_table = self.selib.find_element(self.locator.table).get_attribute('outerHTML')
        page_table = pd.read_html(html_table)[0].loc[:, ["Number", "User", "Description"]]
        page_table['Description'] = page_table['Description'].map(lambda x: x.rstrip('  Vip'))
        return page_table

    @keyword("I select 'vip' checkbox for Sergey Ivan")
    def select_ivan_vip_checkbox(self):
        self.selib.find_element(self.locator.sergey_ivan_vip_checkbox).click()

    @keyword("I should see logs about interaction with VIP checkbox")
    def should_logs_about_vip_checkbox_interaction_exist(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        assert self.selib.find_element(self.locator.log_section)\
                   .text == f'{current_time} Vip: condition changed to true'

    @keyword("I should see expected values in User table")
    def should_user_table_contains_expected_values(self):
        assert self.get_page_table_data().equals(self.__test_dataframe)

    @keyword("I should see 6 VIP checkboxes on page")
    def should_vip_checkboxes_be_presented(self):
        assert len(self.selib.find_elements(self.locator.vip_checkboxes)) == 6

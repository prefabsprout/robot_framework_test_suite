from datetime import datetime

import pandas as pd
from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from selenium.webdriver.support.select import Select


class UserTablePage(PageObject):
    PAGE_URL = "/jdi-light/user-table.html"

    _locators = {
        "sergey_ivan_vip_checkbox": "css:#ivan",
        "log_section": "xpath://ul[@class='panel-body-list logs']//li[1]",
        "table": "xpath://table",
        "vip_checkboxes": "css:[type='checkbox']",
        "number_type_dropdowns": "xpath://td/select",
        "roman_dropdown": "xpath://tbody/tr[1]/td[2]/select"
    }

    __test_data = {'Number': [1, 2, 3, 4, 5, 6],
                   'User': ["Roman", "Sergey Ivan", "Vladzimir", "Helen Bennett", "Yoshi Tannamuri",
                            "Giovanni Rovelli"],
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
        assert self.selib.find_element(self.locator.log_section) \
                   .text == f'{current_time} Vip: condition changed to true', \
            f"Checkbox interaction logs `{self.selib.find_element(self.locator.log_section).text}` is not " \
            f"`{current_time} Vip: condition changed to true` as it expected"

    @keyword("I should see expected values in User table")
    def should_user_table_contains_expected_values(self):
        assert self.get_page_table_data().equals(self.__test_dataframe), \
            "User table content is not equals to expected"

    @keyword("I should see 6 VIP checkboxes on page")
    def should_vip_checkboxes_be_presented(self):
        assert len(self.selib.find_elements(self.locator.vip_checkboxes)) == 6, "Number of VIP checkboxes is not 6"

    @keyword("I should see 6 dropdowns on page")
    def should_number_type_dropdowns_be_presented(self):
        assert len(self.selib.find_elements(self.locator.number_type_dropdowns)) == 6, "Number of dropdowns is not 6"

    @keyword("I should see expected values in any dropdown")
    def should_any_dropdown_contains_expected_values(self):
        dropdown_selector = Select(self.selib.find_element(self.locator.roman_dropdown)).options
        dropdown_elements = [dropdown_element.text for dropdown_element in dropdown_selector]
        expected_dropdown_elements = ["Admin", "User", "Manager"]
        assert dropdown_elements == expected_dropdown_elements, \
            f"{dropdown_elements} is not equal to expected {expected_dropdown_elements}"

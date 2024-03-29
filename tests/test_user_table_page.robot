*** Variables ***
${BROWSER}  chrome
${ROOT}     https://jdi-testing.github.io/jdi-light/index.html
${USERNAME}     Roman
${PASSWORD}     Jdi1234

*** Settings ***
Library     SeleniumLibrary
Library     PageObjectLibrary

Suite Teardown  Close all browsers

*** Test Cases ***
Valid VIP checkboxes presence
    [Documentation]     Verify that User table page contains 6 VIP checkboxes
    Given open browser  ${ROOT}     ${BROWSER}
    And go to page      MainPage
    And I login as user      ${USERNAME}      ${PASSWORD}
    When I click on Service button in Header
    And I click on User Table button in Service dropdown
    And go to page  UserTablePage
    Then I should see 6 VIP checkboxes on page
    And close browser

Valid VIP checkbox functionality
    [Documentation]     Verify that VIP checkboxes work correctly
    Given open browser  ${ROOT}     ${BROWSER}
    And go to page      MainPage
    And I login as user      ${USERNAME}      ${PASSWORD}
    And I click on Service button in Header
    And I click on User Table button in Service dropdown
    And go to page  UserTablePage
    When I select 'vip' checkbox for Sergey Ivan
    Then I should see logs about interaction with VIP checkbox
    And close browser

Valid User table content
    [Documentation]     Verify that User table contains expected content
    Given open browser  ${ROOT}     ${BROWSER}
    And go to page      MainPage
    And I login as user      ${USERNAME}      ${PASSWORD}
    When I click on Service button in Header
    And I click on User Table button in Service dropdown
    And go to page  UserTablePage
    Then I should see expected values in User table
    And close browser

Valid dropdowns
    [Documentation]     Verify that User table contains expected content
    Given open browser  ${ROOT}     ${BROWSER}
    And go to page      MainPage
    And I login as user      ${USERNAME}      ${PASSWORD}
    When I click on Service button in Header
    And I click on User Table button in Service dropdown
    And go to page  UserTablePage
    Then I should see 6 dropdowns on page
    And I should see expected values in any dropdown
    And close browser
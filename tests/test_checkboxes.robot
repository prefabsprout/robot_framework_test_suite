*** Variables ***
${BROWSER}  chrome
${ROOT}     https://jdi-testing.github.io/jdi-light/index.html
${USERNAME}     Roman
${PASSWORD}     Jdi1234

*** Settings ***
Library     SeleniumLibrary
Library     PageObjectLibrary

Suite Setup     open browser    ${ROOT}     ${BROWSER}
Suite Teardown  Close all browsers

*** Test Cases ***
Valid Wind checkbox functionality
    [Documentation]     Verify that Wind checkbox works correctly
    Given go to page      MainPage
    When I login as user      ${USERNAME}      ${PASSWORD}
    And I click on Service button in Header
    And I click on Different Elements button in Service dropdown
    And go to page  DifferentElementsPage
    And I select Wind checkbox
    Then I should see logs about interaction with checkbox  Wind
    And close browser

Valid Water checkbox functionality
    [Documentation]     Verify that Water checkbox works correctly
    Given open browser  ${ROOT}     ${BROWSER}
    And go to page      MainPage
    When I login as user      ${USERNAME}      ${PASSWORD}
    And I click on Service button in Header
    And I click on Different Elements button in Service dropdown
    And go to page  DifferentElementsPage
    And I select Water checkbox
    Then I should see logs about interaction with checkbox  Water
    And close browser
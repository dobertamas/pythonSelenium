Feature: Test navigation between pages
  Longer description here

  Scenario: Admin user can login successfully
    Given I am on the home page
    When I enter credentials
    And I click on Sign in
    Then I am on the console/config/list page
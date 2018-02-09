Feature: Test navigation between pages
  Longer description here

  Scenario: Admin user can login successfully
    Given Admin user is on the home page
    When Admin user enters valid admin credentials
    And Admin user clicks on Sign in button
    Then Admin user is on the Global Preferences page

   Scenario: Admin user can visit the "Push Queue" page
     Given Admin user successfully logged in
     When Admin user clicks on the "Push Queue" link from the pull-down menu


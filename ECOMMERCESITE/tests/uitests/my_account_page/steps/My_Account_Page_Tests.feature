# Created by DivyaSivakumar at 27/08/2020
Feature: My Account Page Tests
  #Tests to validate login with valid, invalid credentials

  Scenario: Valid user should be able to login
    Step I go to 'my account' page

    When I enter 'test@testuser.com' in email field
    And I enter 'passw0rd' in password field
    And I click on 'login' button
    Then User should be logged in

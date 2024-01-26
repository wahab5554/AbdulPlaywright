Feature: API Testing for playwright

  @api @priority_high @regression
    Scenario: Validate API end point
    When  I go to google page
    Then I must see success response
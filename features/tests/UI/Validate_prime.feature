@xf @team_xf_primecelestials @prime_ui @release_sprint_22.05.04
Feature: Xpressfeed prime platform dataset validation
  As an SDET
  I want to verify Xpressfeed prime platform is working fine
  So that user can create and configure datasets

  @priority_high @automated @ui_web @regression
  Scenario: Verify user is able to create dataset
    Given User is login to the prime platform
    When User navigates to Dataset menu option


  Scenario Outline: Verify title for playwright
    When User lands on <url>
    Then User must see <title>
    Examples:
      | url | title |
      | a   | b     |
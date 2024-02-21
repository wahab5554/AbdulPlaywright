@team_cubivue @bk @release_sprint_24.02.13
Feature: BK Cubivue product validation
  As an SQA
  I want to verify BK platform functions are working
  So that user can perform successfull jobs

  @priority_high @automated @ui_web @regression
  Scenario: Verify dashboard page for BK
    Given User is login to the bk platform
    When User lands on main page
    Then User must see total jobs section



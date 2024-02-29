@team_cubivue @kinnarps @iteration_6
Feature: Kinnarps Cubivue product validation
  As an SQA
  I want to verify Kinnarps platform functions are working
  So that user can perform successfull delivery orders


  @priority_high @automated @ui_web @regression
  Scenario: Verify Route Plan Page
    Given User is login to the kinnarps platform
    When I Click on Route Plan bucket
    Then I must see Route Details Tab
    And I must see Map View
    And I must see Activity TimeLine
    And I must see Container Details



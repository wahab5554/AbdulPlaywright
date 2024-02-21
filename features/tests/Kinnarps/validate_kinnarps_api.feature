@team_cubivue @kinnarps @release_sprint_24.02.13
Feature: Kinnarps Cubivue product validation
  As an SQA
  I want to verify Kinnarps platform functions are working
  So that user can perform successfull delivery orders


  @priority_high @automated @api @regression
  Scenario: Verify Kinnarps page load end points
    Given User is login to the kinnarps platform
    Then I must see success response in job status

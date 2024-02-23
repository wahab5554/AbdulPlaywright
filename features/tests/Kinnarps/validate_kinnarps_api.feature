@team_cubivue @kinnarps @iteration_6
Feature: Kinnarps Cubivue product validation
  As an SQA
  I want to verify Kinnarps platform functions are working
  So that user can perform successfull delivery orders


  @priority_high @automated @api @regression
  Scenario Outline: Verify Kinnarps page load end points
    Given User is login to the kinnarps platform
    Then I must see success response from <endpoints>
    Examples:
      | endpoints              |
      | Kinnarps_get_countries |
      | Kinnarps_post_orders   |
      | Kinnarps_get_regions   |
      | Kinnarps_get_terminal  |
      | Kinnarps_get_views     |
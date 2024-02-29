@team_cubivue @kinnarps @iteration_6
Feature: Kinnarps Cubivue product API validation
  As an SQA
  I want to verify Kinnarps platform functions are working
  So that user can perform successfull delivery orders

  @priority_high @automated @api @regression
  Scenario Outline: Verify Route Plan Services
    Given User is login to the kinnarps platform
    When I add multiple <orderids> into <bucketid> using <endpoints>
    Then I must see <orderids> is added in <bucketid> in buckets
    #And I click on empty bucket for <bucketid>
    #And I must not see <orderid> in <bucketid> in buckets
    #And I must see <orderid> in unplanned orders
    Examples:
      | endpoints                  | orderids                          | bucketid  |
      | Kinnarps_add_orders_bucket | 1844382101,1734896900,1906068888 | 229644169 |
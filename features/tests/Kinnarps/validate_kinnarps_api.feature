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
      | endpoints                             |
      | Kinnarps_get_countries                |
      | Kinnarps_post_orders                  |
      | Kinnarps_get_regions                  |
      | Kinnarps_get_terminal                 |
      | Kinnarps_get_views                    |
      | Kinnarps_post_buckets                 |
      | Kinnarps_post_unplanned_orders        |
      | Kinnarps_get_bucketlocationbyid       |
      | Kinnarps_get_planned_orders           |
      | Kinnarps_post_get_bucket_by_id        |
      | Kinnarps_post_get_loading_ramps       |
      | Kinnarps_post_route_details           |
      | Kinnarps_post_route_activity_timeline |
      | Kinnarps_post_route_container_details |
      | Kinnarps_get_vehicles                 |
      | Kinnarps_get_containers               |
      | Kinnarps_get_container_types          |
      | Kinnarps_get_employees                |
      | Kinnarps_get_trailer_types            |
      | Kinnarps_get_transporation_types      |
      | Kinnarps_get_vehicle_types            |
      | Kinnarps_get_employee_types           |
      | Kinnarps_post_users                   |
      | Kinnarps_post_bucket_templates        |
      | Kinnarps_post_route_map               |

  @priority_high @automated @api @regression
  Scenario Outline: Verify Add Order to Bucket in Order Bank
    Given User is login to the kinnarps platform
    When I add <orderid> into <bucketid> using <endpoints>
    Then I must see <orderid> is added in <bucketid> in buckets
    And I click on empty bucket for <bucketid>
    And I must not see <orderid> in <bucketid> in buckets
    And I must see <orderid> in unplanned orders
    Examples:
      | endpoints                  | orderid    | bucketid  |
      | Kinnarps_add_orders_bucket | 1090060409 | 318244937 |


  @priority_high @automated @api @regression
  Scenario Outline: Verify Buckets data is fetched according to weeks filter
    Given User is login to the kinnarps platform
    When I select <week> from top menu
    Then I must see buckets are displayed according to <week>
    Examples:
      | week |
      | 8    |
      | 9    |
      | 7    |
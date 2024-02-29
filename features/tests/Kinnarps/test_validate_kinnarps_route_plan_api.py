from pytest_bdd import *
from features.services.playwright_api import PlaywrightAPI
from pytest_bdd.parsers import parse
obj_playwright_api = PlaywrightAPI()


@scenario('validate_kinnarps_route_plan_api.feature',
          'Verify Route Plan Services')
def test_validate_kinnarps_route_plan_services():
    """Validate Route Plan API end point"""



@given('User is login to the kinnarps platform')
def login():
    obj_playwright_api.login()


@when(parse('I add multiple {orderids} into {bucketid} using {endpoints}'),converters=dict(endpoints=str,orderids=str,bucketid=int))
def validate_response(orderids,bucketid,endpoints):



    payload = obj_playwright_api.generate_payload_multiple_orderids(orderids,bucketid)
    obj_playwright_api.validate_request(endpoints, payload=payload)



@then(parse('I must see {orderids} is added in {bucketid} in buckets'),converters=dict(orderids=str,bucketid=int))
def validate_response(orderids,bucketid):
    end_point = "Kinnarps_get_planned_orders_filter"
    obj_playwright_api.validate_request(end_point, filter=bucketid)

    obj_playwright_api.validate_order(orderids)





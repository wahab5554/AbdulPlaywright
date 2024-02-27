from pytest_bdd import *
from features.services.playwright_api import PlaywrightAPI
from pytest_bdd.parsers import parse
obj_playwright_api = PlaywrightAPI()


@scenario('validate_kinnarps_api.feature',
          'Verify Kinnarps page load end points')
def test_validate_kinnarps_api():
    """Validate API end point"""

@scenario('validate_kinnarps_api.feature',
          'Verify Add Order to Bucket in Order Bank')
def test_validate_add_order_bucket():
    """Verify Add Order to Bucket in Order Bank"""

@scenario('validate_kinnarps_api.feature',
          'Verify Buckets data is fetched according to weeks filter')
def test_validate_buckets_week_data():
    """Verify Buckets data is fetched according to weeks filter"""
@given('User is login to the kinnarps platform')
def login():
    obj_playwright_api.login()


@then(parse('I must see success response from {endpoints}'),converters=dict(endpoints=str))
def validate_response(endpoints):

    obj_playwright_api.validate_request(endpoints)


@when(parse('I add {orderid} into {bucketid} using {endpoints}'),converters=dict(orderid=int,bucketid=int,endpoints=str))
def validate_response(orderid,bucketid,endpoints):

    payload=obj_playwright_api.modify_payload(orderid,bucketid,endpoints)
    obj_playwright_api.validate_request(endpoints,payload=payload)


@when(parse('I select {week} from top menu'),converters=dict(week=int))
def validate_week(week):
    endpoints='Kinnarps_post_buckets'
    payload=obj_playwright_api.weeks_payload(week,endpoints)
    obj_playwright_api.validate_request(endpoints,payload=payload)

@then(parse('I must see {orderid} is added in {bucketid} in buckets'),converters=dict(orderid=int,bucketid=int))
def validate_response(orderid,bucketid):
    end_point="Kinnarps_get_planned_orders_filter"
    obj_playwright_api.validate_request(end_point,filter=bucketid)

    obj_playwright_api.validate_order(orderid)


@then(parse('I click on empty bucket for {bucketid}'),converters=dict(bucketid=int))
def validate_response(bucketid):
    end_point="Kinnarps_post_remove_orders_bucket"
    payload = obj_playwright_api.modify_payload_bucket(bucketid, end_point)
    obj_playwright_api.validate_request(end_point,payload=payload)


@then(parse('I must not see {orderid} in {bucketid} in buckets'),converters=dict(orderid=int,bucketid=int))
def validate_response(bucketid,orderid):
    end_point="Kinnarps_get_planned_orders_filter"
    obj_playwright_api.validate_request(end_point, filter=bucketid)

    obj_playwright_api.validate_removed_order(orderid)

@then(parse('I must see {orderid} in unplanned orders'),converters=dict(orderid=int))
def validate_response(orderid):
    end_point="Kinnarps_post_unplanned_orders"
    obj_playwright_api.validate_request(end_point)

    obj_playwright_api.validate_unplanned_orders(orderid)


@then(parse('I must see buckets are displayed according to {week}'),converters=dict(week=int))
def validate_response(week):

    obj_playwright_api.validate_week_data(week)


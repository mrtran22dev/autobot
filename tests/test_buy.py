import pytest
from pytest_bdd import scenario, given, when, then, parsers


@scenario('../features/buy.feature', 'Target - login, add item, checkout')
def test_item_checkout():
    pass

@scenario('../features/buy.feature', 'Target - Product list page sorting and filtering')
def test_plp_sort_filter():
    pass

@scenario('../features/buy.feature', 'Target - Valid/invalid login accounts')
def test_login_accounts():
    pass


# @scenario('../features/buy.feature', 'Test scenario')
# def test_login():
#     pass


# @scenario('../features/buy.feature', 'Snkrs - Poll + add item to cart')
# def test_snkrs():
#     pass



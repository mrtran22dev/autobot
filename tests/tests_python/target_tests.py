import pytest
from pytest_bdd import scenario, given, when, then, parsers


@scenario('../tests/features/target_tests.feature', 'Target - login, add item, checkout')
def test_item_checkout():
    pass

@scenario('../tests/features/target_tests.feature', 'Target - Product list page sorting and filtering')
def test_plp_sort_filter():
    pass

@scenario('../tests/features/target_tests.feature', 'Target - Valid/invalid login accounts')
def test_login_accounts():
    pass





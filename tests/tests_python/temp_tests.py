import pytest
from pytest_bdd import scenario, given, when, then, parsers


@scenario('../tests/features/temp_tests.feature', 'snkrs landing custom method')
def test_snkrs_landing_custom_method():
    pass


@scenario('../tests/features/temp_tests.feature', 'Snkrs - Poll + add item to cart')
def test_snkrs():
    pass
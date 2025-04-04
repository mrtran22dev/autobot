import pytest
from pytest_bdd import scenario, given, when, then, parsers

feature_file = '../features/temp_tests.feature'


@pytest.mark.snkrs
@scenario(feature_file, 'snkrs landing custom method')
def test_snkrs_landing_custom_method():
    pass


@scenario(feature_file, 'walmart landing custom method')
def test_walmart_landing_custom_method():
    pass


@scenario(feature_file, 'Snkrs - Poll + add item to cart')
def test_snkrs():
    pass
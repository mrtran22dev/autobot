import pytest
from pytest_bdd import scenario, given, when, then, parsers
from config import configs

feature_file = configs.ROOT_DIR + '/tests/features/test_target.feature'

# @pytest.mark.checkout
@scenario(feature_file, 'Target - login, add item, checkout')
def test_item_checkout():
    pass


# @pytest.mark.target_sort
@scenario(feature_file, 'Target - Product list page sorting and filtering')
def test_plp_sort_filter():
    pass


@scenario(feature_file, 'Target - Valid/invalid login accounts')
def test_login_accounts():
    pass





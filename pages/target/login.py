from playwright.sync_api import expect, Page
from pytest_bdd import parsers
from config import configs

from pages import base
from utils.utils import *
import types
import logging


class LoginPage(base.BasePage):
    def __init__(self, pw_page, locators: types.ModuleType):
        super().__init__(pw_page)

        # USING SIMPLENAMESPACE:
        # ======================
        self.page_name = 'login'
        self.common = dict_to_namespace(getattr(locators, 'common'))    # Convert common locators
        self.loc = dict_to_namespace(getattr(locators, 'login'))        # Convert page locators

        # Merge common locators with page-specific locators
        for key, val in self.common.__dict__.items():
            if hasattr(self.loc, key):
                getattr(self.loc, key).__dict__.update(val.__dict__)
            else:
                setattr(self.loc, key, val)
        del self.common


@when(parsers.parse('user login to account with username "{user}" and password "{password}"'))
def login_to_account(page: Page, user, password, context):
    expect(page.locator(context.input.user)).to_be_visible(timeout=configs.OBJ_TIMEOUT)
    page.wait_for_timeout(500)
    page.fill(context.input.user, user)
    page.wait_for_timeout(500)
    if page.locator(context.button.login_continue).is_visible(timeout=500):
        page.locator(context.button.login_continue).click()
    expect(page.locator(context.input.password)).to_be_visible(timeout=configs.OBJ_TIMEOUT)
    page.wait_for_timeout(500)
    page.fill(context.input.password, password)
    expect(page.locator(context.button.login)).to_be_visible(timeout=configs.OBJ_TIMEOUT)
    page.click(context.button.login)
    page.wait_for_timeout(1000)
    if page.locator(context.text.login_alert).is_visible(timeout=500):
        page.fill(context.input.password, password)
        page.click(context.button.login)



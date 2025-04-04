from playwright.sync_api import expect, Page
from pytest_bdd import parsers
from config import configs

from pages import base
from utils.utils import *
import types
import logging


class LandingPage(base.BasePage):
    def __init__(self, pw_page, locators: types.ModuleType):
        super().__init__(pw_page)

        # USING SIMPLENAMESPACE:
        # ======================
        self.page_name = 'landing'
        self.common = dict_to_namespace(getattr(locators, 'common'))    # Convert common locators
        self.loc = dict_to_namespace(getattr(locators, 'landing'))        # Convert page locators

        # Merge common locators with page-specific locators
        for key, val in self.common.__dict__.items():
            if hasattr(self.loc, key):
                getattr(self.loc, key).__dict__.update(val.__dict__)
            else:
                setattr(self.loc, key, val)
        del self.common


@when(parsers.parse('walmart landing custom method'))
def snkrs_landing_custom_method(page: Page, context):
    logging.info('walmart landing custom method')
    page.locator('test')


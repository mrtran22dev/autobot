import logging
import types
from pages import base
from utils.utils import *


class LandingPage(base.BasePage):
    def __init__(self, pw_page, locators: types.ModuleType):
        super().__init__(pw_page)

        # USING SIMPLENAMESPACE:
        # ======================
        self.page_name = 'landing'
        self.common = dict_to_namespace(getattr(locators, 'common'))  # Convert common locators
        self.loc = dict_to_namespace(getattr(locators, 'landing'))  # Convert page locators

        # Merge common locators with page-specific locators
        for key, val in self.common.__dict__.items():
            if hasattr(self.loc, key):
                getattr(self.loc, key).__dict__.update(val.__dict__)
            else:
                setattr(self.loc, key, val)
        del self.common

    def custom_landing_method(self):
        logging.info('custom snkrs landing page method')
        self.page.locator('test')



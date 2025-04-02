import types
from pages import base
from utils.utils import *


class ProductPage(base.BasePage):
    def __init__(self, pw_page, locators: types.ModuleType):
        super().__init__(pw_page)

        # USING SIMPLENAMESPACE:
        # ======================
        self.page_name = 'product'
        self.common = dict_to_namespace(getattr(locators, 'common'))  # Convert common locators
        self.loc = dict_to_namespace(getattr(locators, 'product'))  # Convert page locators

        # Merge common locators with page-specific locators
        for key, val in self.common.__dict__.items():
            if hasattr(self.loc, key):
                getattr(self.loc, key).__dict__.update(val.__dict__)
            else:
                setattr(self.loc, key, val)
        del self.common

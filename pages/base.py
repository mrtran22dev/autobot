import logging
from types import SimpleNamespace
from playwright.sync_api import Page



# class AttributeDict(dict):
#     """Wrapper to allow attribute-style access to dictionary keys."""
#     def __getattr__(self, item):
#         if item in self:
#             value = self[item]
#             # Recursively convert nested dicts into AttributeDict
#             if isinstance(value, dict):
#                 return AttributeDict(value)
#             return value
#         raise AttributeError(f"Attribute '{item}' not found")
#
#     def __setattr__(self, key, value):
#         self[key] = value
#
#
# def dict_to_namespace(d):
#     """Convert a dictionary to a SimpleNamespace."""
#     if isinstance(d, dict):
#         return SimpleNamespace(**{k: dict_to_namespace(v) if isinstance(v, dict) else v for k, v in d.items()})
#     return d



class BasePage:
    def __init__(self, page: Page):
        self.page = page

    # def __init__(self, curr_page, site, locators):
    #     self.page = Page
    #
    #     # USING SIMPLENAMESPACE:
    #     # ======================
    #     self.common = dict_to_namespace(getattr(locators, 'common'))  # Convert common locators
    #     self.locators = dict_to_namespace(getattr(locators, curr_page))  # Convert page locators
    #     # Merge common locators with page-specific locators
    #     for key, val in self.common.__dict__.items():
    #         if hasattr(self.locators, key):
    #             getattr(self.locators, key).__dict__.update(val.__dict__)
    #         else:
    #             setattr(self.locators, key, val)
    #     del self.common
    #
    #     # USING ATTRIBUTEDICT WRAPPER:
    #     # ==============================
    #     self.common = AttributeDict(getattr(locators, 'common'))  # Wrap common locators
    #     self.locators = AttributeDict(getattr(locators, curr_page))  # Wrap current page locators
    #     # Merge common locators with page-specific locators
    #     for key, val in self.common.items():
    #         if key in self.locators:
    #             self.locators[key].update(val)
    #         else:
    #             self.locators[key] = val
    #     # Convert to AttributeDict after merging
    #     self.locators = AttributeDict(self.locators)
    #
    #     ORIGINAL:
    #     =========
    #     self.common = getattr(locators, 'common')
    #     self.locators = getattr(locators, curr_page)
    #     for key, val in self.common.items():
    #         self.locators[key].update(self.common[key])






import ast
import os

from pages.snkrs.landing import LandingPage
from playwright.sync_api import Page
from pages import target
from pages import snkrs
from locators import snkrs_locators, target_locators
from config import configs


def page_navigation(site: str, page: str):
    site_page_map = {
        'target': {
            'landing': configs.SITE_TARGET,
            'clearance': '/c/clearance/-/N-5q0ga',
            'furniture_deals': '/c/furniture-sale/-/N-13iww',
            'cart': '/cart',
            'checkout': '/checkout',
        },
        'snkrs': {
            'landing': configs.SITE_SNKRS
        }
    }
    url = site_page_map[site]['landing']

    if page == 'landing':
        return url
    else:
        return url + site_page_map[site][page]


class PageFactory:
    @staticmethod
    def get_page_object(pw_page: Page, page: str, site: str):
        # pages_root = os.environ.get('PROJECT_ROOT', os.path.dirname(os.path.abspath(__file__)))
        # page_file_path = os.path.join(pages_root, site)

        if site == "target":
            page_map = {
                "landing": target.LandingPage,
                "products_list": target.ProductsListPage,
                "login": target.LoginPage,
                "product": target.ProductPage,
                "cart": target.CartPage,
                "checkout": target.CheckoutPage
            }
            try:
                page_object = page_map[page]
            except KeyError:
                raise KeyError(f"No page object defined for '{page}'")
            return page_object(pw_page, locators=target_locators)
        elif site == "snkrs":
            page_map = {
                "landing": snkrs.landing.LandingPage
            }
            try:
                page_object = page_map[page]
            except KeyError:
                raise KeyError(f"No page object defined for '{page}'")
            return page_object(pw_page, locators=snkrs_locators)


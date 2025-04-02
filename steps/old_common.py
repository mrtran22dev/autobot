# from types import SimpleNamespace
#
# import pytest
# from pytest_bdd import scenario, given, when, then, parsers
# from playwright.sync_api import Page, expect
# import logging
#
# from pages import base, page_factory
# from config import configs
#
# from config import login
# from locators.locator_resolver import get_locators
# from locators import target_locators
#
# # methods calls pytest.fixture in conftest.py file first
#
#
# # @then(parsers.parse('user should be on the "{curr_page}" page of "{site}" site'))
# # def validate_page(page: Page, curr_page, site, step_context):
# #     # Fetch locators for the specified site and page
# #     locators = get_locators(site, curr_page)
# #     step_context['locators'] = locators
# #
# #     expect(page.locator(locators['validate']['element'])).to_be_visible()
# #     # Example: Validate presence of an element
# #     # assert page.locator(locators['validate']['element']).is_visible(timeout=15000), "Validation element is not visible"
# #     print(f"Validated locators for page '{curr_page}' on site '{site}'")
#
#
# @when('user pause test')
# def pause(page: Page, context):
#     print('pause test')
#
#
# @then(parsers.parse('user should be on the "{curr_page}" page of "{site}" site'))
# # def validate_page(page: Page, curr_page, site, context):
# def validate_page(page, curr_page: str, site: str, context1):
#     pf = page_factory.PageFactory()
#     page_context = pf.get_page_object(pw_page=page, page=curr_page, site=site)
#     for key, value in page_context.loc.__dict__.items():
#         setattr(context1, key, value)
#     expect(page.locator(page_context.loc.validate.element)).to_be_visible(timeout=configs.PAGE_TIMEOUT)
#     logging.info(f"Validated locators for page '{curr_page}' on site '{site}'")
#
#
# @given(parsers.parse('user navigates to "{url}"'))
# def navigate(page: Page, url):
#     logging.info("Navigating to url ...")
#     page.goto(url)
#
#
# @when(parsers.parse('user clicks on the "{button}" button'))
# def click_button(page: Page, button, context):
#     btn = context.button.__dict__
#     expect(page.locator(btn[button])).to_be_visible(timeout=configs.OBJ_TIMEOUT)
#     page.click(btn[button])
#
#
# @when(parsers.parse('user fills text "{text}" in "{field}" field'))
# def enter_text(page: Page, text, field, context):
#     _input = context.input.__dict__
#     expect(page.locator(_input[field])).to_be_visible(timeout=configs.OBJ_TIMEOUT)
#     page.wait_for_timeout(500)
#     page.fill(_input[field], text)
#
#
# @when(parsers.parse('user clicks on product "{position}" in the products list page'))
# def click_product_list_nth(page: Page, position, context):
#     page.click(context.button.product_nth % str(int(position)-1))
#
#
# @when(parsers.parse('user fills out target username "{user}" and password "{password}" and logs in account'))
# def login_to_account(page: Page, user, password, context):
#     expect(page.locator(context.button.sign_in)).to_be_visible(timeout=configs.OBJ_TIMEOUT)
#     page.click(context.button.sign_in)
#     expect(page.locator(context.button.login_sidebar)).to_be_visible(timeout=configs.OBJ_TIMEOUT)
#     page.click(context.button.login_sidebar)
#     validate_page(page, 'login', 'target', context)
#
#     expect(page.locator(context.input.user)).to_be_visible(timeout=configs.OBJ_TIMEOUT)
#     page.wait_for_timeout(500)
#     page.fill(context.input.user, user)
#     expect(page.locator(context.input.password)).to_be_visible(timeout=configs.OBJ_TIMEOUT)
#     page.wait_for_timeout(500)
#     page.fill(context.input.password, password)
#     # page.click(context['buttons']['login'])
#
#
# @when(parsers.parse('user clicks on first element matching "{text}" text'))
# def click_first_match_text_element(page: Page, text, context):
#     page.get_by_text(text, exact=True).nth(0).click()
#
#
# @when(parsers.parse('user fills out the form based on table'))
# @given(parsers.parse('user fills out the form based on table'))
# def fill_table(page: Page, context, context1):
# # def fill_table(context):
#     users_db = {}
#     for row in context.table:
#         username = row['locator']
#         password = row['value']
#     #     users_db[username] = {'password': password, 'role': role}
#     # print("Users added:", users_db)
#
#
#
#
# # ============================================================================================================
#
# # @then(parsers.parse('user should be on the "{curr_page}" page of "{site}" site'))
# # def validate_page(page: Page, curr_page, site, context):
# #     # Fetch locators for the specified site and page
# #     locators = get_locators(site, curr_page)
# #     context.update(locators)
# #
# #     expect(page.locator(context['validate']['element'])).to_be_visible()
# #     # Example: Validate presence of an element
# #     # assert page.locator(context['validate']['element']).is_visible(timeout=15000), "Validation element is not visible"
# #     print(f"Validated locators for page '{curr_page}' on site '{site}'")
# #
# # @when(parsers.parse('user clicks on the "{button}" button'))
# # def click_for_target(page: Page, button, context):
# #     btn = context['button'][button]
# #     expect(page.locator(btn)).to_be_visible()
# #     page.click(btn)
# #
# #
# # @when(parsers.parse('user fills text "{text}" in "{field}" field'))
# # def enter_text(page: Page, text, context):
# #     expect(page.locator(context['input']['search'])).to_be_visible()
# #     page.wait_for_timeout(500)
# #     page.fill(context['input']['search'], text)
# #
# #
# # @when(parsers.parse('user clicks on product "{position}" in the products list page'))
# # def click_product_list_nth(page: Page, position, context): #, step_context):
# #     page.click(context['button']['product_nth'] % str(int(position)-1))
# #
# #
# # @when(parsers.parse('user fills out username "{user}" and password "{password}" and logs in account'))
# # def enter_text(page: Page, user, password, context):
# #     expect(page.locator(context['button']['sign_in'])).to_be_visible()
# #     page.click(context['button']['sign_in'])
# #     expect(page.locator(context['button']['login_sidebar'])).to_be_visible()
# #     page.click(context['button']['login_sidebar'])
# #
# #     expect(page.locator(context['input']['user'])).to_be_visible()
# #     page.wait_for_timeout(500)
# #     page.fill(context['input']['user'], user)
# #     expect(page.locator(context['input']['password'])).to_be_visible()
# #     page.wait_for_timeout(500)
# #     page.fill(context['input']['password'], password)
# #     # page.click(context['buttons']['login'])
# #
# #
# # @when(parsers.parse('user clicks on first element matching "{text}" text'))
# # def click_first_match_text_element(page: Page, text, context):
# #     page.get_by_text(text, exact=True).nth(0).click()
# #
# #
# #
#
# # ============================================================================================================
#
# # @when(parsers.parse('user clicks on the "{button}" button'))
# # def click_jordan(page: Page, button):
# # # @when("user clicks on jordan")
# # # def click_jordan(page: Page):
# #     logging.info("click_jordan()")
# #     btn = locators.landing[button]
# #     if page.is_visible(btn) and page.locator(btn).count() == 1:
# #         page.click(btn)
# #     logging.info('navigated to Upcoming link')
# #     page.get_by_text('Air Jordan 3', exact=True).scroll_into_view_if_needed()
# #     page.get_by_text('Air Jordan 3', exact=True).click()
# #     page.wait_for_timeout(2000)
# #
# #
# # # @then("on jordan item")
# # # @then(parsers.parse('user verifies product should have text "{text}"'))
# # @then(parsers.parse('user verifies product should have "{text}" text'))
# # def on_jordan_item(page: Page, text):
# #     logging.info("on_jordan_item()")
# #     text = locators.product[text]
# #     expect(page).to_have_title(text)
# #     logging.info('finished')
# #
# #
# # @given(parsers.parse('user login to "{site}"'))
# # def login(page: Page, site):
# #     site_login = getattr(login, site)
# #     # page.set_extra_http_headers({"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'})
# #
# #     page.goto(site_login['url'])
# #     page.click(locators.landing['login'])
# #     expect(page).to_have_title('Welcome to Nike - Sign In')
# #     # page.click(locators.login['input']['username'])
# #     page.fill(locators.login['input']['username'], site_login['user'])
# #     page.click(locators.login['button']['continue'])
# #     page.fill(locators.login['input']['password'], site_login['pw'])
# #     page.click(locators.login['button']['signin'])
# #
# #
# # @when(parsers.parse('user select size "{size}" to cart and proceed to checkout'))
# # def select_size_add_to_cart(page: Page, size):
# #     page.goto('https://www.nike.com/launch/t/air-jordan-3-black-cement')
# #     # size = input('enter shoe size: ')           # TODO: need to run this with 'pytest -s' otherwise throw OSError cause by pytest using input/output capture
# #     page.get_by_text(size).click()
# #     page.click(locators.product['button']['buy'])
# #     page.click(locators.product['button']['checkout'])
#
#
#
#

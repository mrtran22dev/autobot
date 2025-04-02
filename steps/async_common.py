from pytest_bdd import scenario, given, when, then, parsers
from playwright.async_api import Page, expect  # Change to async_api
import logging
from pages import base, page_factory
from config import configs

# Note: Assuming context is SimpleNamespace from conftest.py, no async change needed there

@when('user pause test')
async def pause(page: Page, context):  # Make async even though no Playwright calls here
    print('pause test')

@then(parsers.parse('user should be on the "{curr_page}" page of "{site}" site'))
async def validate_page(page: Page, curr_page: str, site: str, context1):
    pf = page_factory.PageFactory()
    page_context = pf.get_page_object(pw_page=page, page=curr_page, site=site)
    for key, value in page_context.loc.__dict__.items():
        setattr(context1, key, value)
    await expect(page.locator(page_context.loc.validate.element)).to_be_visible(timeout=configs.PAGE_TIMEOUT)
    logging.info(f"Validated locators for page '{curr_page}' on site '{site}'")

@given(parsers.parse('user navigates to "{url}"'))
async def navigate(page: Page, url):
    logging.info("Navigating to url ...")
    await page.goto(url)

@when(parsers.parse('user clicks on the "{button}" button'))
async def click_button(page: Page, button, context):
    btn = context.button.__dict__
    await expect(page.locator(btn[button])).to_be_visible(timeout=configs.OBJ_TIMEOUT)
    await page.click(btn[button])

@when(parsers.parse('user fills text "{text}" in "{field}" field'))
async def enter_text(page: Page, text, field, context):
    _input = context.input.__dict__
    await expect(page.locator(_input[field])).to_be_visible(timeout=configs.OBJ_TIMEOUT)
    await page.wait_for_timeout(500)
    await page.fill(_input[field], text)

@when(parsers.parse('user clicks on product "{position}" in the products list page'))
async def click_product_list_nth(page: Page, position, context):
    await page.click(context.button.product_nth % str(int(position)-1))

@when(parsers.parse('user fills out target username "{user}" and password "{password}" and logs in account'))
async def login_to_account(page: Page, user, password, context):
    await expect(page.locator(context.button.sign_in)).to_be_visible(timeout=configs.OBJ_TIMEOUT)
    await page.click(context.button.sign_in)
    await expect(page.locator(context.button.login_sidebar)).to_be_visible(timeout=configs.OBJ_TIMEOUT)
    await page.click(context.button.login_sidebar)
    await validate_page(page, 'login', 'target', context)  # Already async

    await expect(page.locator(context.input.user)).to_be_visible(timeout=configs.OBJ_TIMEOUT)
    await page.wait_for_timeout(500)
    await page.fill(context.input.user, user)
    await expect(page.locator(context.input.password)).to_be_visible(timeout=configs.OBJ_TIMEOUT)
    await page.wait_for_timeout(500)
    await page.fill(context.input.password, password)

@when(parsers.parse('user clicks on first element matching "{text}" text'))
async def click_first_match_text_element(page: Page, text, context):
    await page.get_by_text(text, exact=True).nth(0).click()

@when(parsers.parse('user fills out the form based on table'))
@given(parsers.parse('user fills out the form based on table'))
async def fill_table(page: Page, context):  # Add page parameter if needed
    users_db = {}
    for row in context.table:
        username = row['locator']
        password = row['value']
        users_db[username] = password
    # If this step needs to interact with page, add async calls here, e.g.:
    # await page.fill(context.input.some_field, users_db['some_locator'])
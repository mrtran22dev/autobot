from pytest_bdd import scenario, given, when, then, parsers
from playwright.sync_api import Page, expect
import logging
from pages import base, page_factory
from config import configs
from pages.target import *


# methods calls pytest.fixture in conftest.py file first


@when('user pause test')
@then('user pause test')
def pause(page: Page, context, bdd_context):
    print('pause test')


@given(parsers.parse('user navigates to "{site}" site "{curr_page}" page'))
@when(parsers.parse('user navigates to "{site}" site "{curr_page}" page'))
def navigate_to_page(page: Page, site: str, curr_page: str, context):
    context.current_page = curr_page
    context.current_site = site
    url = page_factory.page_navigation(site, curr_page)
    page.goto(url)


@given(parsers.parse('user navigates to "{url}"'))
def navigate(page: Page, url):
    logging.info("Navigating to url ...")
    page.goto(url)


@then(parsers.parse('user should be on the "{curr_page}" page of "{site}" site'))
def validate_page(page: Page, curr_page, site, context):
    page.wait_for_load_state(state='domcontentloaded')
    # page.wait_for_load_state(state='networkidle', timeout=configs.OBJ_TIMEOUT)
    pf = page_factory.PageFactory()
    page_context = pf.get_page_object(pw_page=page, page=curr_page, site=site)
    logging.info(f"Validating locators for page '{curr_page}' on site '{site}' ...")
    for key, value in page_context.loc.__dict__.items():
        setattr(context, key, value)
    expect(page.locator(page_context.loc.validate.element)).to_be_visible(timeout=configs.PAGE_TIMEOUT)
    context.current_page = curr_page
    context.current_site = site
    logging.info(f"Validated locators for page '{curr_page}' on site '{site}'")


@when(parsers.parse('user selects by text the "{text_}" element of locator "{loc}" and type "{type_}"'), target_fixture='sorted_prices')
def sort_plp_items(page: Page, text_, loc, type_, context):
    locators = context.__dict__
    locators = locators[type_].__dict__
    expect(page.locator(locators['filter_bar'] % text_)).to_be_visible(timeout=configs.OBJ_TIMEOUT)
    page.click(locators['filter_bar'] % text_)
    expect(page.locator(context.list.sidebar_filter_menu % 'Price: low to high')).to_be_visible(timeout=configs.OBJ_TIMEOUT)
    page.locator(context.list.sidebar_filter_menu % 'Price: low to high').click()
    expect(page.locator(context.button.sidebar_apply)).to_be_visible(timeout=configs.OBJ_TIMEOUT)
    page.locator(context.button.sidebar_apply).click()
    page.wait_for_timeout(timeout=2000)
    page.wait_for_load_state(state="load", timeout=1000)
    page.wait_for_load_state(state="domcontentloaded", timeout=1000)
    # page.wait_for_load_state(state="networkidle", timeout=15000)

    prices = page.locator(context.list.items_price).all_inner_texts()
    return prices

@then(parsers.parse('user verifies prices are sorted in "{order}" order'))
def price_sort_validation(page: Page, order, sorted_prices, context):
    if order == 'ASC':
        exp_sort = sorted(sorted_prices, key=lambda x: float(x.replace('$', '')))
        assert sorted_prices == exp_sort, \
            f"Prices are not sorted in {order} order: {sorted_prices} != {exp_sort}"
    elif order == 'DESC':
        exp_sort = sorted(sorted_prices, key=lambda x: float(x.replace('$', '')), reverse=True)
        assert sorted_prices == exp_sort, \
            f"Prices are not sorted in {order} order: {sorted_prices} != {exp_sort}"
    else:
        raise Exception(f'sorting order: "{order}" is not a valid sorting order')


@when(parsers.parse('user filters the items from price range of "{min_price}" to "{max_price}"'), target_fixture='filtered_prices')
def filter_plp_items(page: Page, min_price, max_price, context):
    expect(page.locator(context.button.filter_bar % 'Filter')).to_be_visible(timeout=configs.OBJ_TIMEOUT)
    page.click(context.button.filter_bar % 'Filter')
    expect(page.locator(context.list.sidebar_filter_menu % 'Price')).to_be_visible(timeout=configs.OBJ_TIMEOUT)
    page.locator(context.list.sidebar_filter_menu % 'Price').click()

    expect(page.locator(context.input.sidebar_filter_min_price)).to_be_visible(timeout=configs.OBJ_TIMEOUT)
    page.fill(context.input.sidebar_filter_min_price, min_price)
    expect(page.locator(context.input.sidebar_filter_max_price)).to_be_visible(timeout=configs.OBJ_TIMEOUT)
    page.fill(context.input.sidebar_filter_max_price, max_price)

    expect(page.locator(context.button.sidebar_apply)).to_be_visible(timeout=configs.OBJ_TIMEOUT)
    page.locator(context.button.sidebar_apply).click()
    page.get_by_text('See results').click()
    page.wait_for_timeout(timeout=2000)
    page.wait_for_load_state(state="load", timeout=1000)
    page.wait_for_load_state(state="domcontentloaded", timeout=1000)
    # page.wait_for_load_state(state="networkidle", timeout=15000)

    prices = page.locator(context.list.items_price).all_inner_texts()
    return prices


@then(parsers.cfparse('user verifies prices are filtered correctly between "{min_price}" to "{max_price}"'))
def price_sort_validation(page: Page, filtered_prices, min_price, max_price):
    for price in filtered_prices:
        assert float(min_price) <= float(price[1:]) <= float(max_price), f'price filter mismatch - price: {price} is not between {min_price}-{max_price}'


@when(parsers.parse('user clicks on the "{button}" button'))
def click_button(page: Page, button, context):
    btn = context.button.__dict__
    expect(page.locator(btn[button])).to_be_visible(timeout=configs.OBJ_TIMEOUT)
    page.click(btn[button])


@when(parsers.parse('user clicks on the "{button}" button if visible'))
def click_butto_if_visible(page: Page, button, context):
    btn = context.button.__dict__
    page.wait_for_load_state(state='domcontentloaded')
    # page.wait_for_load_state(state='networkidle')
    page.wait_for_timeout(500)
    if page.locator(btn[button]).is_visible(timeout=configs.OBJ_TIMEOUT):
        page.click(btn[button])


@when(parsers.parse('user fills text "{text}" in "{field}" field'))
def enter_text(page: Page, text, field, context):
    _input = context.input.__dict__
    expect(page.locator(_input[field])).to_be_visible(timeout=configs.OBJ_TIMEOUT)
    page.wait_for_timeout(500)
    page.fill(_input[field], text)


@when(parsers.parse('user clicks on product "{position}" in the products list page'))
def click_product_list_nth(page: Page, position, context):
    page.click(context.button.product_nth % str(int(position)-1))


@when(parsers.parse('user clicks on first element matching "{text}" text'))
def click_first_match_text_element(page: Page, text):
    page.get_by_text(text, exact=True).nth(0).click()


@when(parsers.parse('user adds item on product page to cart and navigates to checkout page'))
def add_item(page: Page, context, bdd_context):
    expect(page.locator(context.button.delivery)).to_be_visible(timeout=configs.OBJ_TIMEOUT)
    page.click(context.button.delivery)
    expect(page.locator(context.button.add_to_cart)).to_be_visible(timeout=configs.OBJ_TIMEOUT)
    page.click(context.button.add_to_cart)
    expect(page.locator(context.button.decline_coverage_sidebar)).to_be_visible(timeout=configs.OBJ_TIMEOUT)
    page.click(context.button.decline_coverage_sidebar)
    navigate_to_page(page, site=context.current_site, curr_page='checkout', context=context)
    bdd_context.cleanup.append(f'{context.current_site}_clear_cart')


@when("fills out form based on table", target_fixture="table_data")   # target_fixture here stores datatable values in a fixture named 'users' that can we used in next steps. do not need to declare global viarables
def _(page: Page, context, datatable):
    input_loc = context.input.__dict__
    headers = datatable[0]
    for row_data in datatable[1:]:
        for index, header in enumerate(headers):
            tag = page.locator(input_loc[header]).evaluate("element => element.tagName")
            if tag == 'INPUT':
                page.fill(input_loc[header], row_data[index])
            elif tag == 'SELECT':
                page.locator(input_loc[header]).select_option(row_data[index])
            else:
                raise ValueError(f"tag: '{tag}' is not found")
        return datatable

@then(parsers.parse('the "{button}" button should be visible'))
def validate_element_visible(page: Page, button, context):
    btns = context.button.__dict__
    expect(page.locator(btns[button])).to_be_visible(timeout=configs.OBJ_TIMEOUT)





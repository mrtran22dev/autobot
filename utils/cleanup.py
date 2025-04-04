from pages import base, page_factory
# from playwright.async_api import Page, async_playwright, expect, Browser
from playwright.sync_api import Page, sync_playwright, expect, Browser
import logging
from config import configs


def teardown_resolver(page: Page, bdd_context, curr_page=None, site=None):
    teardowns = {
        'target_clear_cart': clear_cart
    }
    for teardown in bdd_context.cleanup:
        teardowns[teardown](page)


def create_pf(page: Page, site, curr_page):
    url = page_factory.page_navigation(site, curr_page)
    page_object = page_factory.PageFactory.get_page_object(page, curr_page, site)
    return url, page_object


def clear_cart(page, site=None, curr_page=None, context=None):
    logging.info('Cleanup of cart items after scenario executing ...')
    url, page_object = create_pf(page, curr_page='cart', site='target')
    page.goto(url)
    expect(page.locator(page_object.loc.button.delete_item)).to_be_visible(timeout=configs.OBJ_TIMEOUT)
    page.click(page_object.loc.button.delete_item)





    # with sync_playwright() as playwright:
    #     browser = playwright.chromium.launch(headless=False)
    #     browser_context = browser.new_context(
    #         user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    #         viewport={"width": 1500, "height": 900},
    #         locale="en-US",
    #     )
    #     page = browser_context.new_page()
    #
    #     url = page_factory.page_navigation(site, 'cart')
    #     page_object = page_factory.PageFactory.get_page_object(page, 'cart', site)
    #     page.goto('https://www.google.com')
    #
    #     logging.info(f"Navigated to {url} for cleanup")
    #
    #     # Cleanup
    #     page.close()
    #     browser_context.close()
    #     browser.close()



# async def clear_cart(site: str, context):
#     logging.info('cleanup of cart items after scenario executing ...')
#     async with async_playwright() as playwright:
#         browser = await playwright.chromium.launch(headless=False)
#         browser_context = await browser.new_context(
#             user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
#             viewport={"width": 1500, "height": 900},
#             locale="en-US",
#         )
#         page = await browser_context.new_page()
#
#         url = page_factory.page_navigation(site, 'cart')
#         page_object = page_factory.PageFactory.get_page_object(page, 'cart', site)
#         await page.goto('https://www.google.com')
#
#         logging.info(f"Navigated to {url} for cleanup")
#
#         # Cleanup
#         await page.close()
#         await browser_context.close()
#         await browser.close()

    # expect(page.locator(context.button.delete_item)).to_be_visible(timeout=configs.OBJ_TIMEOUT)
    # page.click(context.button.delete_item)
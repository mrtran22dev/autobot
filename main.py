import asyncio
import time

from pages import page_factory
from config import environment, configs
# from playwright.sync_api import Page, sync_playwright
import logging
from playwright.async_api import async_playwright, Playwright, Page, Browser, expect

logging.basicConfig(level=logging.INFO)

''' To run application, goto 'dist/main' folder and enter ./main'''

async def run(playwright: Playwright): #, browser_name: str, url: str):
    logging.info('Started browser context setup + launching browser')
    browser = await playwright.chromium.launch(headless=configs.HEADLESS, channel=configs.BROWSER)  # Use headless=True to run in headless mode
    # Create a browser context
    context = await browser.new_context(
        user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        viewport={"width": 1500, "height": 900},
        locale="en-US",
        # geolocation={"latitude": 38.3928, "longitude": -122.7507},  # santa rosa
        # permissions=["geolocation"]
    )

    # Open a new page
    page = await context.new_page()
    # yield page
    return page, browser


async def goto_site(playwright: Playwright, browser_name: str, url: str, wait_time: int):
    # async for page in run(playwright):        # for if you use 'yield page' in run()
    page, browser = await run(playwright)
    try:
        logging.info(f'navigating to site: {url}')
        await page.goto(url)
        await page.wait_for_timeout(wait_time)
        return browser_name
    finally:
        await page.close()
        await browser.close()



# ========================================================================================

async def target_task1(playwright: Playwright):
    page, browser = await navigate_to_target(playwright)
    pf = page_factory.PageFactory()
    po = pf.get_page_object(pw_page=page, page='landing', site='target')
    await add_first_search_item_to_cart_and_login(page, pf, po)


async def navigate_to_target(playwright: Playwright):
    page, browser = await run(playwright)
    await page.goto('https://www.target.com')
    return page, browser


async def add_first_search_item_to_cart_and_login(page: Page, pf: page_factory.PageFactory, page_object: page_factory.Page):
    po = page_object
    search = await search_target(page=page, page_object=po)
    po = pf.get_page_object(pw_page=page, page='products_list', site='target')
    await page.click(po.loc.button.product_nth % str(int(0)))
    po = pf.get_page_object(pw_page=page, page='login', site='target')
    await login_target(page=page, page_object=po)


async def search_target(page: Page, page_object, browser: Browser = None):
    po = page_object
    await expect(page.locator(po.loc.validate.element)).to_be_visible(timeout=configs.PAGE_TIMEOUT)
    logging.info(f"Validated locators for page 'landing' on site 'target'")
    # user input
    text = input('enter search text: ')
    await expect(page.locator(po.loc.button.search)).to_be_visible(timeout=configs.OBJ_TIMEOUT)
    await page.fill(po.loc.input.search, text)
    await page.click(po.loc.button.search)
    return text

    # loc = page_object.loc
    # await expect(page.locator(loc.validate.element)).to_be_visible(timeout=configs.PAGE_TIMEOUT)
    # logging.info(f"Validated locators for page 'landing' on site 'target'")
    # # user input
    # text = input('enter search text: ')
    # await expect(page.locator(loc.button.search)).to_be_visible(timeout=configs.OBJ_TIMEOUT)
    # await page.fill(loc.input.search, text)
    # await page.click(loc.button.search)
    # return text


async def login_target(page: Page, page_object):
    po = page_object
    await page.click(po.loc.button.sign_in)
    await page.click(po.loc.button.login_sidebar)

    user = input('enter account name to login: ')
    pw = input('enter account password: ')
    await expect(page.locator(po.loc.input.user)).to_be_visible(timeout=configs.OBJ_TIMEOUT)
    await page.wait_for_timeout(500)
    await page.fill(po.loc.input.user, user)
    await expect(page.locator(po.loc.input.password)).to_be_visible(timeout=configs.OBJ_TIMEOUT)
    await page.wait_for_timeout(500)
    await page.fill(po.loc.input.password, pw)


async def main():
    async with async_playwright() as playwright:
        logging.info('Autobot started ...')

        """ Test automation with page factory + objects """
        tasks = [
            target_task1(playwright),
            goto_site(playwright, browser_name='browser1 completed', url='https://www.google.com', wait_time=3000)
        ]
        await asyncio.gather(*tasks)

        # ===========================================================================================
        # tasks = [
        #     goto_site(playwright, browser_name='browser1 completed', url='https://www.google.com', wait_time=3000),
        #     goto_site(playwright, browser_name='browser2 completed', url='https://www.duckduckgo.com', wait_time=1000),
        # ]
        #
        # """ Use asyncio.gather() - schedules tasks and await completion of coroutines; and gets/returns results in order of tasks list"""
        # results = await asyncio.gather(*tasks)
        # logging.info(results)

        # ===========================================================================================
        # """ Create/schedules both tasks individually, then await completion via asyncio.gather() """
        # """ Create/schedules both tasks """
        # task1 = asyncio.create_task(
        #     goto_site(playwright, browser_name='browser1 completed', url='https://www.google.com', wait_time=3000))
        # task2 = asyncio.create_task(
        #     goto_site(playwright, browser_name='browser2 completed', url='https://www.duckduckgo.com', wait_time=1000))
        # """ Wait for both tasks to finish """
        # results = await asyncio.gather(task1, task2)
        # # Log the results
        # for result in results:
        #     logging.info(result)

        # ===========================================================================================
        """ Use asyncio.as_completed to get results in the order of completion """
        # results = []
        # for task in asyncio.as_completed(tasks):
        #     result = await task
        #     results.append(result)
        # logging.info(results)


if __name__ == '__main__':
    asyncio.run(main())




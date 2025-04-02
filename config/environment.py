import asyncio
import logging
import pytest
from playwright.async_api import async_playwright, Page
from playwright.sync_api import sync_playwright, Page
from config import configs
from typing import AsyncGenerator

# config/environment.py
import asyncio
import logging
import pytest
# from playwright.async_api import async_playwright, Page
from playwright.async_api import async_playwright, Page

from config import configs



# async def browser_context() -> Page:
#     # Launch the browser
#     logging.info('Started browser context setup + launching browser')
#     async with async_playwright() as playwright:
#         browser = await playwright.chromium.launch(headless=configs.HEADLESS, channel=configs.BROWSER)
#
#         # Create a browser context
#         context = await browser.new_context(
#             user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
#             viewport={"width": 1500, "height": 900},
#             locale="en-US",
#         )
#
#         # Open a new page
#         page = await context.new_page()
#         yield page
#
#         # Close the context and browser
#         await context.close()
#         await browser.close()



def browser_context() -> Page:
    # Launch the browser
    logging.info('Started browser context setup + launching browser')
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=configs.HEADLESS, channel=configs.BROWSER)  # Use headless=True to run in headless mode

        # Create a browser context
        context = browser.new_context(
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            viewport={"width": 1500, "height": 900},
            locale="en-US",
            # geolocation={"latitude": 38.3928, "longitude": -122.7507},  # santa rosa
            # permissions=["geolocation"]
        )

        # Open a new page
        page = context.new_page()
        # page = stealth_sync(page)
        yield page

        # # Close the context and browser
        context.close()
        browser.close()


# @pytest.fixture
# async def page(browser_context):
#     return await browser_context.new_page()



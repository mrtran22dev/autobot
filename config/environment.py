from playwright.sync_api import sync_playwright, Page
from config import configs
import asyncio
import logging
import pytest
from config import configs


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





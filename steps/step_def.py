from pytest_bdd import scenario, given, when, then, parsers
from playwright.sync_api import Page, expect
import logging
from config import configs


@when(parsers.parse('user login to account with username "{user}" and password "{password}"'))
def login_account(page: Page, context, user, password):
    expect(page.locator(context.input.user)).to_be_visible(timeout=configs.OBJ_TIMEOUT)
    page.wait_for_timeout(500)
    page.fill(context.input.user, user)
    expect(page.locator(context.input.password)).to_be_visible(timeout=configs.OBJ_TIMEOUT)
    page.wait_for_timeout(500)
    page.fill(context.input.password, password)
    expect(page.locator(context.input.login)).to_be_visible(timeout=configs.OBJ_TIMEOUT)
    page.click(context.input.login)
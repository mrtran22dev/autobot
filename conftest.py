from types import SimpleNamespace

import pytest
from steps.common import *
from config import environment
from playwright.sync_api import Page
from utils import cleanup
import os
import importlib
# from pages.snkrs import landing


# BDD statements/methods calls pytest.fixture in conftest.py file

# Site configuration and module imports
# base_pages_dir = os.path.join(os.path.dirname(__file__), 'pages')
# site_config = {
#     # 'target': {'locators': importlib.import_module('locators.target_locators'), 'pages_dir': os.path.join(base_pages_dir, 'target')},
#     # 'snkrs': {'locators': importlib.import_module('locators.snkrs_locators'), 'pages_dir': os.path.join(base_pages_dir, 'snkrs')}
#     'target': {'pages_dir': os.path.join(base_pages_dir, 'target')},
#     'snkrs': {'pages_dir': os.path.join(base_pages_dir, 'snkrs')}
# }
#
# page_modules = {}
# for site, config in site_config.items():
#     page_modules[site] = {}
#     pages_dir = config['pages_dir']
#     for filename in os.listdir(pages_dir):
#         if filename.endswith('.py') and filename != '__init__.py':
#             module_name = filename[:-3]
#             module = importlib.import_module(f'pages.{site}.{module_name}')
#             page_modules[site][module_name] = module

@pytest.fixture
def page() -> Page:
    logging.info("fixture loaded from conftest.py")
    yield from environment.browser_context()


@pytest.fixture(scope="function")
def context():
    """A shared context for steps to store data like locators."""
    return SimpleNamespace(current_page=None, current_site=None)


# Fixture to access the pytest-bdd internal context
@pytest.fixture(scope="function")
def bdd_context(request):
    # Retrieve the context stored in the request.config
    return getattr(request.config, "bdd_context", None)


def pytest_bdd_before_scenario(request, feature, scenario):
    logging.info('Before scenario setup executing ...')
    logging.info(f'{feature.name} -> {scenario.name}')
    # context.__setattr__('cleanup', False)                           # this is a different context, part of pytest-bdd?
    bdd_context = SimpleNamespace()
    bdd_context.cleanup = []
    request.config.bdd_context = bdd_context


def pytest_bdd_before_step(request, feature, scenario, step):
    logging.info(f'{feature.name} -> {scenario.name} -> {step.name}')
    request.config.bdd_context.step = step.name


def pytest_bdd_after_scenario(request, feature, scenario):
    logging.info('After scenario teardowns executing ...')
    logging.info(f'{feature.name} -> {scenario.name}')
    page = request.getfixturevalue('page')
    bdd_context = request.config.bdd_context
    # context = request.getfixturevalue('context')                  # this gets custom fixture: context
    curr_page = request.getfixturevalue('context').current_page
    site = request.getfixturevalue('context').current_site
    if bdd_context.cleanup:
        cleanup.teardown_resolver(page, bdd_context, curr_page, site)


# # Dynamic fixture creation loop
# for site, modules in page_modules.items():
#     locators = site_config[site]['locators']
#     for module_name in modules:
#         module = modules[module_name]
#         page_class = None
#         for attr_name in dir(module):
#             attr = getattr(module, attr_name)
#             if isinstance(attr, type) and attr_name.endswith('Page'):
#                 page_class = attr
#                 break
#         if not page_class:
#             raise ValueError(f"No page class found in pages/{site}/{module_name}.py")
#
#         @pytest.fixture(scope="function")
#         def page_fixture(page: Page, _page_class=page_class, _locators=locators):
#             return _page_class(page, _locators)
#         fixture_name = f"{site}_{module_name}_page"
#         globals()[fixture_name] = page_fixture




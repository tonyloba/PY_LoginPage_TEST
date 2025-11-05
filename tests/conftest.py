import os
import pytest
import pytest_html
from pathlib import Path
from utils.driver_factory import get_driver

# Ensure reports directory exists
Path('reports').mkdir(exist_ok=True)

@pytest.fixture(scope="session")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

from pytest_html import extras

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            screenshot = driver.get_screenshot_as_base64()
            report.extra = getattr(report, "extra", [])
            report.extra.append(extras.image(screenshot, mime_type='image/png'))


import pytest
from utils.driver_manager import get_driver


@pytest.fixture
def browser():
    driver = get_driver()
    yield driver
    driver.quit()


def test_open_example(browser):
    browser.get("https://example.com")
    assert "Example Domain" in browser.title


@pytest.mark.parametrize("url", [
    "https://example.com",
    "https://www.google.com"
])
def test_open_sites(browser, url):
    browser.get(url)
    assert browser.title != ""
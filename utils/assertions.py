
from playwright.sync_api import expect


def verify_element_visible(locator):

    expect(locator).to_be_visible()


def verify_element_text(locator, expected):

    expect(locator).to_have_text(expected)


def verify_element_contains_text(locator, expected):

    expect(locator).to_contain_text(expected)


def verify_element_count(locator, expected_count):

    expect(locator).to_have_count(expected_count)


def verify_url(page, expected_url):

    expect(page).to_have_url(expected_url)

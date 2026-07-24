import re
from playwright.sync_api import Page, expect  # type: ignore


def test_dropdown(page: Page):
    page.goto("https://practice-automation.com/form-fields/")

    page.wait_for_timeout(3000)
    dropdown = page.locator("#automation")
    options = dropdown.locator("option")
    expect(options).to_have_count(4)
    expected_data = [
        ("default", ""),
        ("yes", "Yes"),
        ("no", "No"),
        ("undecided", "Undecided"),
    ]
    for i in range(len(expected_data)):
        expect(options.nth(i)).to_have_attribute("value", expected_data[i][0])

import re
from playwright.sync_api import Page, expect  # type: ignore[import]


def test_iframe(page: Page):
    page.goto("https://practice-automation.com/iframes/")

    top_frame = page.frame_locator("#iframe-1")
    page.wait_for_timeout(3000)
    expect(top_frame.locator("body")).to_contain_text("playwright")

    bottom_frame = page.frame_locator("#iframe-2")
    page.wait_for_timeout(3000)
    expect(bottom_frame.locator("body")).to_contain_text("Selenium")
    page.wait_for_timeout(3000)

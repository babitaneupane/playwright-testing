# import re
from playwright.sync_api import Page, expect  # type: ignore[import]


def test_has_title(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    page.locator(
        "//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']"
    ).click()
    page.wait_for_timeout(5000)

    page.go_back()
    page.wait_for_timeout(5000)
    page.go_forward()

    page.wait_for_timeout(5000)

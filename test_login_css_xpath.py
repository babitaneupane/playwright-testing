import re
from playwright.sync_api import Page, expect  # type: ignore


def test_has_title(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # page.locator("input[placeholder='Username' ]").fill("Admin")
    # page.locator("input[placeholder='Password']").fill("admin123")
    # page.locator("button[type='submit' ]").click()                  //css locator inspect ma gayera selectorshub .. to run pytest test.... --headed
    page.locator("//input[@placeholder='Username']").fill("Admin")
    page.locator("//input[@placeholder='Password']").fill("admin123")
    page.locator(
        "//button[normalize-space()='Login']"
    ).click()  # xpath  same as prev but relxpath

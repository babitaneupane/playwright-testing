import re
from playwright.sync_api import Page, expect  # type: ignore[import]


def test_has_title(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.locator("//input[@placeholder='Username']").fill("standard_user")
    page.locator("//input[@placeholder='Password']").fill("secret_sauce")
    page.locator("#login-button").click()

    # product1 = page.locator(".inventory_item").filter(has_text="sauce Labs Bike Light")
    # product1.locator("button:has-text('Add to cart')").click()
    # page.wait_for_timeout(5000)

    product1 = page.locator(".inventory_item").filter(
        has=page.locator("button.btn_inventory")
    )
    product1.first.locator("button").click()
    page.wait_for_timeout(15000)

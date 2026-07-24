import re
from playwright.sync_api import Page, expect  # type: ignore[import]


def test_webtable(page: Page):
    page.goto("https://practice-automation.com/tables/")
    page.wait_for_timeout(3000)
    table = page.locator("table").first
    page.wait_for_timeout(3000)
    rows = table.locator("tr")
    expect(rows).to_have_count(3)

    for i in range(rows.count()):
        cells = rows.nth(i).locator("td")
    if cells.count() > 0 and cells.nth(0).inner_text() == "Oranges":
        expect(cells.nth(1)).to_have_text("$3.99")

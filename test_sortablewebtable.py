from playwright.sync_api import Page, expect


def test_webtable(page: Page):
    page.goto("https://practice-automation.com/tables/")
    page.wait_for_timeout(3000)
    table = page.locator("table").nth(1)
    page.wait_for_timeout(3000)
    rows = table.locator("tr")
    expect(rows).to_have_count(11)
    expect(rows.first).to_be_visible()
    page.locator("text=population(million)").click()
    page.wait_for_timeout(3000)
    population_list = []
    for i in range(rows.count()):
        cells = rows.nth(i).locator("td")
        population_text = cells.nth(2).inner_text()
        clean_value = population_text.replace(",", "")
        population_list.append(clean_value)
        print("Actual Population Values", population_list)
        expected_sorted_list = sorted(population_list)
        assert population_list == expected_sorted_list

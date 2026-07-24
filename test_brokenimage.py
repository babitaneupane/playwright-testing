import re
from playwright.sync_api import Page, expect  # type: ignore[import]
from urllib.parse import urljoin


def test_broken_image(page: Page):
    page.goto("https://practice-automation.com/broken-images/")
    page.wait_for_timeout(3000)
    images = page.locator("img")
    broken_images = []

    for i in range(images.count()):
        src = images.nth(i).get_attribute("src")
        if not src:
            continue
        image_url = urljoin(page.url, src)
        response = page.request.get(image_url)
        if response.status == 404:
            broken_images.append(image_url)
            print(f"\nTotal Broken Images:{len(broken_images)}")
            for url in broken_images:
                print("Broken Image URL:", url)


from playwright.async_api import async_playwright
import asyncio

# Function to scrape with Playwright
async def scrapeWithPlaywright(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(url)

        all_houses = await page.query_selector_all('.post-inner')

        data = []
        for house in all_houses:
            # price = await house.query_selector('.price')
            title = await house.query_selector('.post-title')
            data.append({
                # 'price': await price.inner_text(),
                'title': await title.inner_text()
            })
        print(data)
        # await page.screenshot(path=f'py_1.png', full_page=True)
        content = await page.content()
        await browser.close()
        return content

url1 = "https://turaheza.com/category/amazu-akodeshwa/"

content = asyncio.run(scrapeWithPlaywright(url1))
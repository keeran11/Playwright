#here extracting the titles of the following link

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://news.ycombinator.com/')
    
    titles = page.locator('.storylink')
    for i in range(titles.count()):
        print(f"{i+1}: {titles.nth(i).inner_text()}")
    
    browser.close()

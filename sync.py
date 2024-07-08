from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = chromium.launch(headless=False)#Running in headless mode means that the browser operates without a visible UI
    #If it is set it to "true" the browser will open with a visible user interface. This mode is often used during the 
    # development and debugging of automation scripts because it allows you to see what the browser is doing.
    page = browser.new_page()
    page.goto("https://www.whatismybrowser.com/") #link of the website where to scrape
    page.screenshot(path="demo.png")
    page.wait_for_timeout(3000)
    browser.close()
with sync_playwright() as playwright:
    run(playwright)
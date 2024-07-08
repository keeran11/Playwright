from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser =p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://demo.automationtesting.in/Register.html')

    #hover for the dropwon
    # page.wait_for_selector('//a[text() = "SwitchTo"]').hover()

    #for click
    # page.wait_for_selector('//a[text() = "SwitchTo"]').click()

    #for doubleclick
    # page.wait_for_selector('//a[text() = "SwitchTo"]').dblclick()

    #for rightclick
    page.wait_for_selector('//a[text() = "SwitchTo"]').click(button="right")

    #for shift key
    page.wait_for_selector('//a[text() = "SwitchTo"]').click(modifiers=["Shift"])

    #keyboard action
    page.wait_for_selector('//a[text() = "SwitchTo"]').press("A")

    #A-z , 0-9 , F1 -F12, all special character, arrowRight, ArrowDown, PageUP, Enter, control,command
    page.wait_for_selector('//a[text() = "SwitchTo"]').press("$")

    

    page.wait_for_timeout(2000)


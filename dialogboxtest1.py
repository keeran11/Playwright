#task is that goto alert with textbox and click it and type something in the alert box.

from playwright.sync_api import sync_playwright
text_alert = [ ] #global variable

def handle_dialoge(dialog):
    message =dialog.message
    text_alert.append(message)
    dialog.accept()

with  sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/Alerts.html')

    page.wait_for_selector('//div[@id = "Textbox"]/button').click()
    page.on('dialog', lambda dialog: dialog.accept(message= "Hello world"))

    page.wait_for_timeout(300)
    print(text_alert)



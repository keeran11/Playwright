
from playwright.sync_api import sync_playwright


text_alert = []#global varaible

def handle_dialoge(dialog):
    message = dialog.message #storing the message coming form the dialoge
    text_alert.append(message)#here appending to the global variable
    dialog.accept()


with sync_playwright()  as p:
    browser = p.chromium.launch(headless = False)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/Alerts.html')

    #here parent tag ko id use garera child ko tag use garara nikaalni
    # //div[@id = "OKTab"]/button
    #here "/" is direct child if given // it tells any child,grand child
    #in this link there the button is only one so given direct child

#in playwright ma alert lai dialog vaninxa
#dialog is the alert and in lambda will create dialog and say to dialog click on accept

    # page.on("dialog", lambda dialog: dialog.accept()) #accept hunxa
    # page.on("dialog", lambda dialog: dialog.dismiss())
    # page.on("dialog", lambda dialog: print(dialog.message)) #this will show the dialoge message
    #tester we have to validate test is wright or wrong
#above is for old method

#control alert
    page.on("dialog", handle_dialoge)


    

    page.wait_for_selector('//div[@id = "OKTab"]/button').click()
    #here in the playwright will alert and automatically click ok button
    #to verify the alert button it click ok button


    page.wait_for_timeout(2000)
    print(text_alert[0])




#radio button and check box
#radio button is the buton where we can select only one option 

#check box is in the square manner where we can select many option


from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/Register.html")
#select best xpath here value is giving the meaningfull data so we take value
#//input[@value='FeMale']
    radio_button = page.query_selector('//input[@value = "FeMale"]')
    #there are two option it will hellps

    radio_button.click()
    #if statement in python
    if radio_button.is_checked():
        print("passed")
    else:
        print("failed")


    #checkBox

    checkbox = page.query_selector('//input[@id = "checkbox1"]')
    checkbox.click()
    if checkbox.is_checked():
        print("passed")
    else:
        print("failed")


    page.wait_for_timeout(3000)

#there are two types of dropdown
#1. select dropdown
# 2. bootstrap dropdown

from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/Register.html')


    #select dropdown
    #1. find the select location
    #which to choose xpath for select we type, class, id, ng-model,nf-init(which are attributes)
    #best thing to choose is id
    #//tagename[@id = "value"]
    #//select[@id = "Skills"]
    # select_dropdown = page.query_selector('//select[@id = "Skills"]')

    # #2. selcet the option
    # select_dropdown.select_option(label ='Art Design')

#here is the second option that we can solve to find the dropdown option

    page.select_option('//select[@id = "Skills"]', label='AutoCAD')


    page.wait_for_timeout(5000)





# <input id = "email" , type ="text" placeholder="Email id for sign up" ng-model="emailid" autofocus>
#first is tag and second is attributes

from playwright.sync_api import sync_playwright


with sync_playwright() as play:
    browser =play.chromium.launch(headless=False)
    page = browser.new_page()
    # page.goto('https://demo.automationtesting.in/Index.html')
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')


    #cssSelector - id= #, class = . , attribute tagname[aatibute = "value"]

    #id

    # emailtxtbix = page.wait_for_selector('#email')
    # emailtxtbix.type('test@gmail.com') # here it will type the test@gmail.com
    # buttonlogin = page.wait_for_selector('#enterimg')
    # buttonlogin.click()



    #attribute= tagname[aatibute = "value"]

    username = page.wait_for_selector('input[name = "username"]')
    username.type("Admin")
    password = page.wait_for_selector('input[type = "password"]')
    password.type("admin123")
    buttonlogin =page.wait_for_selector('button[type="submit"]')
    buttonlogin.click()


    page.wait_for_timeout(3000)
    


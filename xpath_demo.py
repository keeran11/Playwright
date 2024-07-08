from playwright.sync_api import sync_playwright



with sync_playwright() as p:
    browser = p.chromium.launch(headless= False)
    page = browser.new_page()
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')


    #xpath: easy to understand and easy to travels between the development
    #there is relative Xpath and absoulute Xpath
    #xpath -Relative xpath '//'
    #using attribute - //tagname[@attributename= "value"]
    #while slecting the attribute should be unique
    #for selecting the unique attibute in the inspect press ctrl+f and paste the x-path
    #  it and see the if it is hilighted or not


    # username_element = page.wait_for_selector('//input[@name = "username"]')
    # username_element.type('Admin')
    # passworrd_element = page.wait_for_selector('//input[@name ="password"]')
    # # passworrd_element = page.wait_for_selector('//input[@placeholder ="Password"]')

    # passworrd_element.type('admin123')
    # button_element = page.wait_for_selector('//button[@type ="submit"]')
    # button_element.click()


#text = //tagname[text()="text"]   sometime we can use text also
    page.wait_for_selector('//p[text()="Forgot your password? "]').click()

#difference between text and content 
#text should be match exactly what is there on a screen 
#content should not be match



#contains
#attributes = //tagname[contains(@attributes, "value")]
#//input[contains(@placeholder,"Use")]

#text - //tagname[contains(text(), "name of text")]
# text - //label[contains(text(),  "Username")]

# dynamic xpath and dynamic locator - kiran123, kiran1234, kiran4
#starts-with:= //tagname[starts-with(@id, 'kiran')]

#end - with
# // 2343user

#family
#parent, //tagname[@id = "xy"]/parent::input[]
#  child, //tagname[@id = 'xy]/child::input[]
#  ancestor: grate grand parents
#sibling

#in the table there is company contact country and how will you find company and contact only
#company=microsoft  , Contact = Ronald mendel , country : austria
# microsoft and asutria are the sibling 

#sibling = //td[text() = "Microsoft"]//following-sibling::td[2]
           # //td[text() = "hover"]//following-sibling::td[4]

    page.wait_for_timeout(3000)

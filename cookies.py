#what is cookies and cache
#ookies and cache are both used by web browsers to store information, but they serve different purposes and contain different types of data.
#when you login to any website it will store certain datas for there reference future
# to make run fast.
#it store only in the browser.


from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page= context.new_page()


    page.goto('https://www.facebook.com/')

    #gives all the cookies
    my_cookies =page.context.cookies()
    print(my_cookies)
#clear the all the cookies
    page.context.clear_cookies()

#     new_cookies ={
#         'name' : "kiran",
#         'udid' : '4365df41fd'

#     }
# #To pass the new cookies to the page
#     page.context.add_cookies([new_cookies])


#taking screenshot
    page.screenshot(path='test.png' , full_page=True)


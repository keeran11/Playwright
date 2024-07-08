#extracting all the test form "https://demo.automationtesting.in/Selectable.html"

# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     context =browser.new_context()
#     page =context.new_page()
#     page.goto('https://demo.automationtesting.in/Selectable.html')


#     #our task is to get all the element from <b> tag
#     #storing multiple elements using list
    
#     # elements = page.query_selector_all('b')

#     #to Extract all the link form that page 
#     elements = page.query_selector_all('a')

#     print(len(elements))
#     for i in elements:
#         # print(i.text_content())
#         print(i.get_attribute('href')) #it will print all the href:
    
#     page.wait_for_timeout(2000)



    #try catch exception handeling
    #if there is 14 line of code there is worng in 6th line and how to identify where i am wrong
    #to solve this the exception handeling 
    #many ways to handel 
    #try catch is mostly used

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    try:
        browser = p.chromium.launch(headless=False)
        context =browser.new_context()
        page =context.new_page()
        page.goto('https://demo.automationtesting.in/Selectable.html')


        #our task is to get all the element from <b> tag
        #storing multiple elements using list
    
        # elements = page.query_selector_all('b')
        page.query_selector_all('d//[@sdfa]').click()

        #to Extract all the link form that page 
        elements = page.query_selector_all('a')

        print(len(elements))
        for i in elements:
            # print(i.text_content())
            print(i.get_attribute('href')) #it will print all the href:
    
        page.wait_for_timeout(2000)

    except Exception as e:
        print(str(e))

    #exception occur then got to exception if not then finally block code will exicute
    finally:
        print('Execute')





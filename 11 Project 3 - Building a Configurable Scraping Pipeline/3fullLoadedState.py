from playwright.sync_api import sync_playwright

URL='https://store.steampowered.com/specials'

if __name__=='__main__':
    with sync_playwright() as p:
    # False=makes the browser pops up, True=no browser popup
        browser=p.chromium.launch(headless=True)        
        page=browser.new_page()
        page.goto(URL)

    # wait for some element to render
        # page.wait_for_selector('div.classname')
             
    # stop when no more network calls are there
        page.wait_for_load_state('networkidle')         
    
    # give playwright anonymous JS function to evaluate (scroll to bottom)
        page.evaluate('()=>window.scroll(0,document.body.scrollHeight)')    

        page.screenshot(path='steam.png',full_page=True)
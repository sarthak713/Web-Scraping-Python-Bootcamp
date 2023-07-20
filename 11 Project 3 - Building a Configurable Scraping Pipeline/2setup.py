from playwright.sync_api import sync_playwright
# sync_api = synchronous api 

URL='https://store.steampowered.com/specials'

if __name__=='__main__':
# using sync_playwright as context manager
# we need to launch a new browser than open a new page in it
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto(URL)
# Now, we head over to website
# playwright starts rendering all JS that initial html doc points to
        page.screenshot(path='steam.png',full_page=True)
        # take a screenshot when loaded at end
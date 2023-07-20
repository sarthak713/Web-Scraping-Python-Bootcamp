from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser

URL = 'https://store.steampowered.com/specials'

if __name__ == '__main__':
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(URL)

        # this waits until there are no network connections or communications for at least 0.5 secs
        page.wait_for_load_state('networkidle')
        page.evaluate('()=>window.scroll(0,document.body.scrollHeight)')

        # this will consider itself complete when browser fires 'domcontentloaded' event
        page.wait_for_load_state('domcontentloaded') 

        # we can also wait for the content we need to be loaded
        page.wait_for_selector('div[class^="salepreviewwidgets_StoreSaleWidgetContainer"]')   

        html = page.inner_html('body')
        tree = HTMLParser(html)

        divs=tree.css('div[class^="salepreviewwidgets_StoreSaleWidgetContainer"]')

        print(len(divs))

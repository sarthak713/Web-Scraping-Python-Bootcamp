from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser

URL = 'https://store.steampowered.com/specials'

if __name__ == '__main__':

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(URL)

        page.wait_for_load_state('networkidle')
        page.evaluate('()=>window.scroll(0,document.body.scrollHeight)')
        page.wait_for_load_state('domcontentloaded')
        page.wait_for_selector('div[class^="salepreviewwidgets_StoreSaleWidgetContainer"]')

        html = page.inner_html('body')
        tree = HTMLParser(html)

        divs = tree.css('div[class^="salepreviewwidgets_StoreSaleWidgetContainer"]')

        for d in divs:
            title = d.css_first('div[class*="StoreSaleWidgetTitle"]').text()
            thumbnail = d.css_first('img[class*="CapsuleImage"]').attributes.get('src')
            tags = [a.text() for a in d.css('a[class*="salepreviewwidgets_Tag"][href*="tags"]')[:5]]
            release_date = d.css_first('div[class*="WidgetReleaseDateAndPlatform"] > div[class*="StoreSaleWidgetRelease"]').text()
            review_score = d.css_first('div[class*="ReviewScoreValue"] > div').text()
            reviewed_by = d.css_first('div[class*="ReviewScoreCount"]').text()
            original_price = d.css_first('div[class*="StoreOriginalPrice"]').text()
            sale_price = d.css_first('div[class*="StoreSalePriceBox"]').text()
            attrs = {
                'title': title,
                'thumbnail': thumbnail,
                'original_price': original_price,
                'sale_price': sale_price,
                'release_date': release_date,
                'review_score': review_score,
                'reviewed_by': reviewed_by,
                'tags': tags
            }
            print(attrs)

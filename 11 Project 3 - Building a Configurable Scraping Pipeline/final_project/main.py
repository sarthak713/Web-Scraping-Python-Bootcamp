from extract import extract_full_body_html
from myparse import parse_raw_attributes
from tools import get_config
from selectolax.parser import HTMLParser
from processing import format_and_transform
from processing import save_to_file


if __name__ == '__main__':

    config = get_config()

    html = extract_full_body_html(
        from_url=config.get('url'),
        wait_for=config.get('container').get('selector')
    )

    tree = HTMLParser(html)

    divs = tree.css(config.get('container').get('selector'))

    game_data = []

    for d in divs:

        attrs = parse_raw_attributes(d, config.get('item'))
        attrs = format_and_transform(attrs)
        game_data.append(attrs)
        save_to_file('extract.csv', game_data)

        # title = d.css_first('div[class*="StoreSaleWidgetTitle"]').text()
        # thumbnail = d.css_first('img[class*="CapsuleImage"]').attributes.get('src')
        # release_date = d.css_first('div[class*="WidgetReleaseDateAndPlatform"] > div[class*="StoreSaleWidgetRelease"]').text()
        # review_score = d.css_first('div[class*="ReviewScoreValue"] > div').text()
        # reviewed_by = d.css_first('div[class*="ReviewScoreCount"]').text()
        # original_price = d.css_first('div[class*="StoreOriginalPrice"]').text()
        # sale_price = d.css_first('div[class*="StoreSalePriceBox"]').text()
        # tags = [a.text() for a in d.css('a[class*="salepreviewwidgets_Tag"][href*="tags"]')[:5]]

        # attrs = {
        #     'title': title,
        #     'thumbnail': thumbnail,
        #     'original_price': original_price,
        #     'sale_price': sale_price,
        #     'release_date': release_date,
        #     'review_score': review_score,
        #     'reviewed_by': reviewed_by,
        #     'tags': tags
        # }

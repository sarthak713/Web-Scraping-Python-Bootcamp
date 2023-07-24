import json

_config = {
    'url': 'https://store.steampowered.com/specials',
    'container': {
        'name': 'store_sale_divs',
        'selector': 'div[class*="salepreviewwidgets_StoreSaleWidgetContainer"]',
        'match': 'all',
        'type': 'node'
    },
    'item': [
        {
            'name': 'title',
            'selector': 'div[class*="StoreSaleWidgetTitle"]',
            'match': 'first',
            'type': 'text'
        },
        {
            'name': 'thumbnail',
            'selector': 'img[class*="CapsuleImage"]',
            'match': 'first',
            'type': 'node'
        },
        {
            'name': 'tags',
            'selector': 'a[class*="salepreviewwidgets_Tag"][href*="tags"]',
            'match': 'all',
            'type': 'text'
        },
        {
            'name': 'release_date',
            'selector': 'div[class*="WidgetReleaseDateAndPlatform"] > div[class*="StoreSaleWidgetRelease"]',
            'match': 'first',
            'type': 'text'
        },
        {
            'name': 'review_score',
            'selector': 'div[class*="ReviewScoreValue"] > div',
            'match': 'first',
            'type': 'text'
        },
        {
            'name': 'reviewed_by',
            'selector': 'div[class*="ReviewScoreCount"]',
            'match': 'first',
            'type': 'text'
        },
        {
            'name': 'price_currency',
            'selector': 'div[class*="StoreSalePriceBox"]',
            'match': 'first',
            'type': 'text'
        },
        {
            'name': 'original_price',
            'selector': 'div[class*="StoreOriginalPrice"]',
            'match': 'first',
            'type': 'text'
        },
        {
            'name': 'sale_price',
            'selector': 'div[class*="StoreSalePriceBox"]',
            'match': 'first',
            'type': 'text'
        }
    ]
}


def get_config(load_from_file=False):
    if load_from_file:
        with open('config.json', 'r') as f:
            return json.load(f)
    return _config


def generate_config():
    with open('11 Project 3 - Building a Configurable Scraping Pipeline/final_project/config.json', 'w') as f:
        json.dump(_config, f, indent=4)


generate_config()

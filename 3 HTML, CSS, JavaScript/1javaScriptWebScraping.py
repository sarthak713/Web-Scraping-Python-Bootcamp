'''

JavaScript
    - heavily used in modern web pages
    - single page application (SPA) phenom
    - implications for web scraping:
        - what you see is not what you get
            - many websites usually just send html css and a basic js file and js later injects a lot of code into the DOM 
            - if the network inspection of a page is loading many js files after reload it is the indication that a website is using js to inject data & is a SPA
            - we can also use Page Source to check the html
            - SPA needs to be rendered in a headless browser for us to scrape successfully
        - headless browser help
            - great use case to tackle scraping SPA
            - a bit slower as we need to load up the full browser, have it render th page & extract HTML from it
            - lot faster than a browser that visually loads but slower than text based problematic approach through which most sites are scraped mostly

'''
'''

A Useful Mental Model : Course Steps

1. The Web
    = website, web app, any web resource sitting on server
    Tools - requests, httpx, playwright to access resource
2. Parsed/Processes 
    = we send request to server to get resource & then we run it through some interpretation logic
    = when we get a hold of a website it is just text, we have to give it meaning and then extract useful part from it
    Tools - beautifulsoup, selectolax for parsing
3. Loaded/Extracted 
    = in the end we export the data
    = or we load it to some processing pipeline that extracts some insight from that data
    Tools - csv, json, xml, sql to load & save
4. Scrapy
    = integrated web scraping framework
    = binds all above pipeline in one tightly structured framework

'''
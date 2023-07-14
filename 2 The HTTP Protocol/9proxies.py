'''
Proxies
    - an application layer, intermediary server

- HTTP is a stateless communication protocol between client & server
- in practice, due to layered nature of internet, req-res messages pass through multiple intermediaries
- before they reach their destination
- when they operate in application layer, intermediaries are called proxies
- Proxy is just another server that sits b/w client making request, and ther server that will provide response

- Proxy does very specific functional oritented task

- Example: - Caching Proxy, stores copy of response message locally, so when request is made to server, 
           cache proxy first searches response in cache & sends back if exists, if not then makes request to server
           This makes the process faster
           - Load Balancer proxy: server that distributes the load of incoming request across multiple servers
           If millions of request are getting to server, it distributes those request across multiple machines so overloading is avoided

In web scraping, when we access high info from website
We want to cycle through diff IPs so we don't get blocked
SmartProxy: provides pool of IPs that scraping client use to make request to target server
            so residential proxies act as intermediary 
            We make 10k request from one IP, but Residential proxy makes it look like 1 request from 10k different IPs to server

'''
'''
Status Codes

- Client sends lots of requests to server
- which server takes care of handling
- server uses status codes to communicate back to client

Status Code
    - 3 digit number set back to client with each response
        - 1st digit: general category
        - 2nd digit: sub category
        - 3rd digit: even more specific sub category

5 Classes of Status Codes:

1. 100s
    - informational 
    - Example 101 switching protocols
2. 200s
    - success
    - Example 201 created, 204 no content
3. 300s
    - redirection
    - Example 301 moved permanently, 307 temporary redirect
4. 400s
    - client errors
    - Example 404 not found, 403 forbidden, 405 method not allowed
5. 500s
    - server errors
    - Example 500 internal server error, 502 bad gateway

'''
from http.client import HTTPConnection




# 성공
# GET / HTTP/1.1
#  HTTP/1.1 200 OK
conn = HTTPConnection('www.example.com')
conn.request('GET', '/')
resp = conn.getresponse()
print(resp.status, resp.reason)
if resp.status == 200:
    body = resp.read()
    print(body, type(body), sep='\n')


# 실패
# GET /hello.html HTTP/1.1
# HTTP/1.1 404 Not found
conn = HTTPConnection('www.example.com')
conn.request('GET', '/hello.html')
resp = conn.getresponse()
print(resp.status, resp.reason)
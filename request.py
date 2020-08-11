from urllib.parse import urlencode
from urllib.request import urlopen, Request


#get
httpresponse = urlopen('https://www.example.com?a=10&b=20')
body = httpresponse.read()
print(body)


#Post
data = {
    'email':'kicscar@gmail.com',
    'password': '`1234',
    'name' : '안대혁'

}

data = urlencode(data).encode('utf-8')

request = Request('https://www.example.com', data)
request.add_header('content-type', 'text/html')

httpresponse = urlopen(request)
print(httpresponse.read())


# http.client.HttpConnetionn을 사용한 GET방식 요청

from http.client import HTTPConnection

conn = HTTPConnection('www.example.com')
conn.request('GET','/')


result = conn.getresponse()
print(result.status, result.reason) # reason = message

data = result.read()
print(data)















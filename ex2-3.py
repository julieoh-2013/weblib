#post 방식으로 웹서버에 요청 하기
from urllib.request import urlopen, Request
from urllib.parse import urlencode

data = urlencode({'a':10, 'b':20, 'name':'둘리'}) # query 스티링으로 생성 <-> query_qs: dic으로
# data = 'a=10&b=20&name=둘리'

req1 = Request('http://www.example.com/' )

request = Request('http://www.example.com/', data.encode('utf-8'))  #byte 코드 생성

# request 객체를 사용한 request 요청 헤더 변경
request.add_header('Content-Type','text/html')




#post 반식으로 보내기
f = urlopen(request)
print(f.read())





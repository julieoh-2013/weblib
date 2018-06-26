# urlparse lib 테스트

from urllib.parse import urlparse, urlsplit, urljoin, parse_qs # 과제 예제 생성

url = 'http:// www.python.org:80/guido/python.html;philosophy?a=10#here' ##here id 달때 씀, ;philosophy - 파라미터
'''
http://www.aaa.com/hello.html#id_h1
<a href ='id_h1'>here</a>
<h1>asfas</h1>
'''
result = urlparse(url)
print(result)











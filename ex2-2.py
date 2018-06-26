# urlopen

from urllib.request import urlopen

#GET 방식으로 웹 서버에 요청 보내기
f = urlopen('http://www.example.com?a=10&b=2-')
print(f.read())













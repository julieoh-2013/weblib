import os
from html.parser import  HTMLParser
from http.client import HTTPConnection

class ImageParser(HTMLParser): # 클래스 상속
    def handle_starttag(self, tag, attrs): # 함수 오버라이드
        if tag!='img':
            return

        if not hasattr(self, 'result'): #이객체에 result라는 이름의 변수가 없으면 이객체의 result 배열 만들라
            self.result =[]

        for name, value in attrs:
            if name == 'src':
                self.result.append(value)

def main():
    url = 'www.google.co.kr'
    conn = HTTPConnection(url)
    conn.request('GET', '/')

    r = conn.getresponse()
    print(r.status, r.reason)

    data = r.read().decode(encoding='euc-kr')
    conn.close()

    print('\n>>>>>>> Fetch Image From ', url)
    parser = ImageParser()
    parser.feed(data)
    dataset = set(x for x in parser.result)

    #print('\n'.join(sorted(dataset)))




    for d in dataset:
        url = 'www.google.co.kr'
        conn = HTTPConnection(url)
        conn.request('GET', '/%s'%d)
        r = conn.getresponse()
        filename = d.replace('/','_')
        print(filename)
        with open(filename, 'wb') as outfile:  # 자동 클로즈시킴
            outfile.write(r.read())
            outfile.close()


if __name__ == '__main__':
    main()
from urllib.request import urlopen
from html.parser import  HTMLParser

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
    url = 'http://www.google.co.kr'
    response = urlopen(url)
    charset = response.headers.get_content_charset()
    data = response.read().decode(charset)
    response.close()

    print('\n>>>>>>> Fetch Image From ', url)
    parser = ImageParser()
    parser.feed(data)
    dataset = set(x for x in parser.result)
    print('\n'.join(sorted(dataset)))


if __name__ == '__main__':
    main()
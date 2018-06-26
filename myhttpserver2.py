from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO

PORT = 9999
class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        #파라미터가져오기  http://localhost:9999/graph?a=10&b=20
        #1. requestURL찾아내기  /graph  ,http://localhost:9999/board/list
        qindex = self.path.find('?')

        req_url = self.path[:len(self.path)] if qindex == -1 else self.path[:qindex]

        if req_url != '/graph': #path 마다 elsif 등록
            self.send_error(404, 'File Not Found')
            return

        handler_name  = 'ex'+ self.get_parameter('ex')
        if handler_name not in MyHTTPRequestHandler.__dict__: #모든클래스 보유함수를 저장한 변수
            self.send_error(404, 'File Not Found')
            return

        MyHTTPRequestHandler.__dict__[handler_name](self)  # 함수 호출
        
    def get_parameter(self, name):  #param이름 던지면 값을 출력
        qindex = self.path.find('?')

        #parameter 받아오기 querystring 뽑기
        qs = '' if qindex == -1 else self.path[qindex+1:] # ?다음부터 끝까지 가져옴
        params = parse_qs(qs)
        values = params.get(name)

        return None if values is None else values.pop()

    def ex1(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()#개행찍음
        self.wfile.write("<h1>안녕하세요</h1>".encode('utf-8'))

    def ex2(self):
        arr = np.random.normal(5,3,500) # array생성
        fig, subplosts = plt.subplots(2, 1)
        subplosts[0].plot(arr, color='red', linestyle='solid')
        subplosts[1].hist(arr, bins=20, edgecolor='black', linewidth=1.2)


        buffer = BytesIO()
        plt.savefig(buffer, dpi=80, bbox_inches='tight')
        plt.clf() #메모리에 버퍼 flush


        self.send_response(200)
        self.send_header('Content-type', 'image/png')  # minetype정의
        self.end_headers()  # 개행찍음
        self.wfile.write(buffer.getvalue())

#서버구동 : 헨들러 생성, 서버객체 생성하면서 생성한 핸들러 서버에 등록
httpd = HTTPServer(('', PORT), MyHTTPRequestHandler)
print('Server running on port(%d)' % (PORT))
httpd.serve_forever()





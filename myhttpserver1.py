from http.server import BaseHTTPRequestHandler, HTTPServer

port = 9999
class MyHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()#개행찍음
        self.wfile.write("<h1>안녕하세요</h1>".encode('utf-8'))


#서버구동 : 헨들러 생성, 서버객체 생성하면서 생성한 핸들러 서버에 등록
httpd = HTTPServer(('', port), MyHTTPRequestHandler)
print('Server running on port', port)
httpd.serve_forever()
























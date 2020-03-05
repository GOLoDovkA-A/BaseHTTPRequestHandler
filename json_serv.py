from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import cgi

from io import BytesIO

glob_dict = {}

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
        

    def do_GET(self):

        self.send_response(200)

        self.end_headers()

        self.wfile.write(b'Hello, world!')
        

    def do_POST(self):

        content_length = int(self.headers['Content-Length'])

        body = self.rfile.read(content_length)

        body = json.loads(body)

        print("Got object: {}".format(body))

        self.send_response(200)

        self.send_header('content-type','text/html')

        glob_dict = body

        print(glob_dict['load'][1:-1].split(","))

        self.end_headers()

        self.wfile.write(b"received json_mass!")

try :
    httpd = HTTPServer(('localhost', 9502), SimpleHTTPRequestHandler)
    httpd.serve_forever()

except KeyboardInterrupt:
    httpd.server_close()

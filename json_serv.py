from http.server import HTTPServer, BaseHTTPRequestHandler
from collections import Counter, defaultdict
import json
import cgi
import re

global_list = []
word = ""
regex = r"\b\w+\b"

def to_anagram_dict(words):
    anagrams = defaultdict(list)
    for word in words:
        hist = tuple(sorted(Counter(word).items(), key= lambda word_tuple: word_tuple[0]))
        anagrams[hist].append(word)
    return anagrams

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
        
    def do_GET(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        word = re.findall(regex, body.decode())[-1]
        anagrams_list = to_anagram_dict(global_list)[tuple(sorted(Counter(word).items(),key= lambda word_tuple: word_tuple[0]))]
        self.wfile.write(str(anagrams_list).encode())

    def do_POST(self):

        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        body = json.loads(body)
        print("Got object: {}".format(body))
        self.send_response(200)
        self.send_header('content-type','text/html')
        global global_list
        global_list = (re.findall(regex, body["load"]))
        print(global_list)
        self.end_headers()
        self.wfile.write(b"received json_mass!")

try :
    httpd = HTTPServer(('localhost', 9502), SimpleHTTPRequestHandler)
    httpd.serve_forever()

except KeyboardInterrupt:
    httpd.server_close()

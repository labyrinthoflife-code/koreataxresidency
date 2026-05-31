import http.server
import socketserver

PORT = 3000
DIRECTORY = "/Users/changhyunsim/Library/CloudStorage/OneDrive-개인/조세/거주자, 비거주자 진단사이트"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, format, *args):
        print(format % args, flush=True)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}", flush=True)
    httpd.serve_forever()

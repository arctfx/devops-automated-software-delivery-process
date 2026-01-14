import http.server
import socketserver

PORT = 3000

def foo():
    return "Hello World!"

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Always return "Hello World!"
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello World!")

def main():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving on port {PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    main()

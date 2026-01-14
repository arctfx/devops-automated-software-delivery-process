import http.server
import socketserver

PORT = 3000

def foo():
    return "Hello World!"

def bar(x, y):
    """Dummy function for coverage"""
    return x + y

def baz(s):
    """Another dummy function"""
    return s.upper()

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Always return "Hello World!"
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello World!")

def main():
    # ThreadingTCPServer allows multiple concurrent connections
    with socketserver.ThreadingTCPServer(("", PORT), Handler) as httpd:
        print(f"Serving on port {PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    main()

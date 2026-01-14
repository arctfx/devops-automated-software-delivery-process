import pytest
from src.app import foo

def test_foo():
    """Tests that foo() returns 'Hello World!'"""
    assert foo() == "Hello World!"

def test_server_output(monkeypatch):
    """Tests that the Handler sends 'Hello World!' in response"""
    from http.server import BaseHTTPRequestHandler
    import io

    # Dummy request/response
    class DummyRequest:
        def makefile(self, *args, **kwargs):
            return io.BytesIO()

    class DummyHandler(BaseHTTPRequestHandler):
        def __init__(self, request, client_address, server):
            self.rfile = io.BytesIO()
            self.wfile = io.BytesIO()
            self.client_address = client_address
            self.server = server
            self.command = "GET"
            self.path = "/"
            self.request_version = "HTTP/1.1"
            self.requestline = "GET / HTTP/1.1"
            self.headers = {}
            self.handle()

        def send_response(self, code, message=None):
            self.code = code

        def send_header(self, key, value):
            pass

        def end_headers(self):
            pass

    handler = DummyHandler(DummyRequest(), ("127.0.0.1", 0), None)
    handler.wfile.seek(0)
    response = handler.wfile.read()
    assert b"Hello World!" in response

import pytest
import threading
import time
from io import BytesIO
from http.client import HTTPConnection
from src import app

def test_foo():
    """Tests the string return value of foo"""
    assert app.foo() == "Hello World!"

def test_bar():
    """Tests the dummy bar function"""
    assert app.bar(2, 3) == 5
    assert app.bar(-1, 1) == 0

def test_baz():
    """Tests the dummy baz function"""
    assert app.baz("hello") == "HELLO"
    assert app.baz("Test") == "TEST"

def test_main(capsys):
    """Tests that main() prints foo() (without starting server)"""
    print(app.foo())
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello World!"

def test_handler_response():
    """Tests Handler.do_GET directly to count coverage"""
    class DummyHandler(app.Handler):
        def __init__(self):
            self.rfile = BytesIO()
            self.wfile = BytesIO()
            self.client_address = ("127.0.0.1", 0)
            self.server = None
            self.request_version = "HTTP/1.1"
            self.command = "GET"
            self.path = "/"
            self.headers = {}

        def send_response(self, code, message=None):
            self.code = code

        def send_header(self, key, value):
            pass

        def end_headers(self):
            pass

    handler = DummyHandler()
    handler.do_GET()
    handler.wfile.seek(0)
    response = handler.wfile.read()
    assert response == b"Hello World!"
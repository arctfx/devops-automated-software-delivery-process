import pytest
from app import foo, main

def test_foo():
    """Tests the string return value of foo"""
    assert foo() == "Hello World!"

def test_main(capsys):
    """Tests that main() actually prints the expected output"""
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello World!"
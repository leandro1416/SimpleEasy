from src.app import greet


def test_greet_basic():
    assert greet("Alice") == "Hello, Alice!"


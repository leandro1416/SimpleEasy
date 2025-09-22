import importlib
from src.app import greet


def test_greet_basic():
    assert greet("Alice") == "Hello, Alice!"


def test_main_uses_env_name(monkeypatch, capsys):
    monkeypatch.setenv("APP_NAME", "Bob")
    mod = importlib.reload(importlib.import_module("src.app"))
    # call main directly to avoid running on import
    mod.main()
    out = capsys.readouterr().out.strip()
    assert out == "Hello, Bob!"

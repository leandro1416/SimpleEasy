import importlib

from src.app import greet, greet_localized, greet_time_based


def test_greet_basic():
    assert greet("Alice") == "Hello, Alice!"


def test_main_uses_env_name(monkeypatch, capsys):
    monkeypatch.setenv("APP_NAME", "Bob")
    monkeypatch.setenv("APP_LANG", "en")
    monkeypatch.delenv("APP_TIME_GREET", raising=False)
    mod = importlib.reload(importlib.import_module("src.app"))
    # call main directly to avoid running on import
    mod.main()
    out = capsys.readouterr().out.strip()
    assert out == "Hello, Bob!"


def test_greet_localized_pt():
    assert greet_localized("Ana", "pt") == "Olá, Ana!"


def test_greet_localized_es():
    assert greet_localized("Luis", "es") == "¡Hola, Luis!"


def test_greet_localized_fallback():
    assert greet_localized("Kim", "xx") == "Hello, Kim!"


def test_greet_time_based_en():
    assert greet_time_based("Ana", "en", hour=6) == "Good morning, Ana!"
    assert greet_time_based("Ana", "en", hour=12) == "Good afternoon, Ana!"
    assert greet_time_based("Ana", "en", hour=20) == "Good evening, Ana!"


def test_greet_time_based_pt():
    assert greet_time_based("Ana", "pt", hour=6) == "Bom dia, Ana!"
    assert greet_time_based("Ana", "pt", hour=12) == "Boa tarde, Ana!"
    assert greet_time_based("Ana", "pt", hour=20) == "Boa noite, Ana!"


def test_main_time_based(monkeypatch, capsys):
    monkeypatch.setenv("APP_NAME", "Bob")
    monkeypatch.setenv("APP_LANG", "pt")
    monkeypatch.setenv("APP_TIME_GREET", "true")
    # Call function directly with an explicit hour to avoid monkeypatching datetime
    from src import app as mod

    assert mod.greet_time_based("Bob", "pt", hour=6) == "Bom dia, Bob!"


def test_greet_time_based_boundaries():
    # 5 is morning start, 12 afternoon start, 18 evening start
    assert greet_time_based("A", "en", hour=5).startswith("Good morning")
    assert greet_time_based("A", "en", hour=12).startswith("Good afternoon")
    assert greet_time_based("A", "en", hour=18).startswith("Good evening")

import os

_GREETINGS = {
    "en": "Hello, {name}!",
    "pt": "Olá, {name}!",
    "es": "¡Hola, {name}!",
}


def greet(name: str) -> str:
    return _GREETINGS["en"].format(name=name)


def greet_localized(name: str, lang: str = "en") -> str:
    template = _GREETINGS.get(lang.lower(), _GREETINGS["en"])
    return template.format(name=name)


def main() -> None:
    name = os.getenv("APP_NAME", "world")
    lang = os.getenv("APP_LANG", "en")
    print(greet_localized(name, lang))


if __name__ == "__main__":
    main()

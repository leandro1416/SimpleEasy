import os
from typing import Optional

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
    use_time = os.getenv("APP_TIME_GREET", "false").lower() in {"1", "true", "yes", "on"}
    if use_time:
        print(greet_time_based(name, lang))
    else:
        print(greet_localized(name, lang))


def greet_time_based(name: str, lang: str = "en", hour: Optional[int] = None) -> str:
    # Determine hour if not provided
    if hour is None:
        try:
            from datetime import datetime

            hour = datetime.now().hour
        except Exception:
            hour = 12

    # Define periods: morning [5,12), afternoon [12,18), evening otherwise
    if 5 <= hour < 12:
        period = "morning"
    elif 12 <= hour < 18:
        period = "afternoon"
    else:
        period = "evening"

    messages = {
        "en": {
            "morning": "Good morning, {name}!",
            "afternoon": "Good afternoon, {name}!",
            "evening": "Good evening, {name}!",
        },
        "pt": {
            "morning": "Bom dia, {name}!",
            "afternoon": "Boa tarde, {name}!",
            "evening": "Boa noite, {name}!",
        },
    }

    lang_key = lang.lower() if lang.lower() in messages else "en"
    template = messages[lang_key][period]
    return template.format(name=name)


if __name__ == "__main__":
    main()

import os


def greet(name: str) -> str:
    return f"Hello, {name}!"


def main() -> None:
    name = os.getenv("APP_NAME", "world")
    print(greet(name))


if __name__ == "__main__":
    main()


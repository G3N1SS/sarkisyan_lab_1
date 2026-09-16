"""Модуль, добавленный в ветке feature (задание 5)."""

from main import greet


def greet_many(names: list[str]) -> list[str]:
    """Вернуть список приветствий для нескольких имён."""
    return [greet(name) for name in names]


if __name__ == "__main__":
    for line in greet_many(["Git", "GitHub", "Python"]):
        print(line)

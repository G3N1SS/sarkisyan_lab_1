"""Тесты для main.py и feature.py (выполняются в GitHub Actions)."""

from feature import greet_many
from main import greet


def test_greet_default():
    """Приветствие по умолчанию обращается к Git."""
    assert greet() == "Hello, Git!"


def test_greet_with_name():
    """Приветствие подставляет переданное имя."""
    assert greet("Areg") == "Hello, Areg!"


def test_greet_many():
    """greet_many возвращает по одному приветствию на каждое имя."""
    assert greet_many(["A", "B"]) == ["Hello, A!", "Hello, B!"]

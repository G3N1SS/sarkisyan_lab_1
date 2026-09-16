# Лабораторная работа №1. Система контроля версий Git

Саркисян Арег Седракович, группа 220042-11, вариант 5, лабораторная №1

## Отчет по заданиям

### Средней сложности

* **Задание 1 — установить Git и настроить имя, email.** Установлен Git 2.48.1 (`git --version`). Глобальная настройка выполнена командами `git config --global user.name "Areg Sarkisyan"` и `git config --global user.email "areg.sarkisyan.99@mail.ru"`. Фактический вывод `git --version` и `git config --global --list`, а также автор первого коммита (`12f45cf`) сохранены в `git_setup.txt` (коммит `049c35e`).
* **Задание 5 — создать ветку `feature`, добавить новый файл.** Командой `git checkout -b feature` создана ветка, в ней добавлен файл `feature.py` (коммит `41d3128 feat: add feature.py in feature branch`). Затем ветка слита в `main` через `git merge --no-ff feature` — merge-коммит `7f08e37` с двумя родителями виден в `git log --graph`. Ветка `feature` сохранена и запушена на GitHub.
* **Задание 7 — создать файл `.gitignore` для Python.** Добавлен `.gitignore` (коммит `d3a56cb`) с исключениями из методички (`__pycache__/`, `*.pyc`, `.env`) и дополнительными (`.venv/`, `.pytest_cache/`, файлы IDE и ОС). Работа проверена: сгенерированы `__pycache__/` (через `python3 -c "import main"`) и `.env`, после чего `git status --ignored` показывает их с пометкой `!!`, а `git check-ignore -v` указывает на сработавшие строки `.gitignore`. Вывод сохранён в `gitignore_check.txt` (коммит `4cf7b8a`).

### Повышенной сложности

* **Задание 6 — настроить GitHub Actions для проверки Python-кода.** Создан workflow `.github/workflows/python-check.yml` (коммит `07154f6`). Он запускается при `push` в `main`/`feature` и при `pull_request` в `main`, выполняется на `ubuntu-latest` в матрице Python 3.10 и 3.12. Шаги: `actions/checkout@v4` (с подмодулями) → `actions/setup-python@v5` → установка `requirements-dev.txt` (flake8, pytest) → `flake8 .` → `python -m py_compile` → `pytest -v`. Для проверки добавлены тесты `test_main.py` и конфиг `.flake8` (коммит `4993296`). Локальный прогон тех же шагов (flake8 без замечаний, 3 теста пройдены) сохранён в `ci_check.txt`; результат запуска на GitHub — во вкладке Actions репозитория.
* **Задание 8 — использовать git submodules.** Командой `git submodule add https://github.com/octocat/Hello-World.git external/hello-world` подключён чужой репозиторий как подмодуль (коммит `85d306d`). В родительском репозитории появился файл `.gitmodules` и запись типа `commit` в дереве (`git ls-tree HEAD external/`), указывающая на зафиксированный коммит подмодуля `7fd1a60`. В `submodule_info.txt` (коммит `f959b99`) приведён вывод `git submodule status`, `git ls-tree`, история подмодуля, а также эксперимент: обычный `git clone` оставляет каталог подмодуля пустым, содержимое появляется после `git submodule update --init --recursive` либо сразу при `git clone --recurse-submodules`.

## Файлы репозитория

| Файл | Назначение |
|------|------------|
| `main.py` | основной модуль проекта с функцией `greet` (первый коммит) |
| `git_setup.txt` | вывод `git --version` и `git config --global --list` (задание 1) |
| `feature.py` | файл, добавленный в ветке `feature` (задание 5) |
| `.gitignore` | исключения для Python-проекта (задание 7) |
| `gitignore_check.txt` | вывод `git status --ignored` и `git check-ignore`, подтверждающий работу `.gitignore` (задание 7) |
| `.github/workflows/python-check.yml` | workflow GitHub Actions: flake8 + py_compile + pytest (задание 6) |
| `test_main.py`, `.flake8`, `requirements-dev.txt` | тесты и конфигурация инструментов, которые запускает CI (задание 6) |
| `ci_check.txt` | локальный прогон шагов workflow перед push (задание 6) |
| `.gitmodules`, `external/hello-world/` | описание и содержимое подмодуля octocat/Hello-World (задание 8) |
| `submodule_info.txt` | отчёт по работе с подмодулем (задание 8) |

## Как воспроизвести проверки локально

```bash
git clone --recurse-submodules <url-репозитория>
cd sarkisyan_lab_1
pip install -r requirements-dev.txt
flake8 .
pytest -v
```

Сообщения коммитов оформлены в стиле Conventional Commits (`feat:`, `docs:`, `chore:`, `test:`, `ci:`).

# tetrika-junior_test
# Тестовое для Тетрики

## Задача 1: Декоратор `@strict`

Реализован декоратор `@strict`, который проверяет соответствие типов аргументов аннотациям функции.

## Задача 2: Животные по алфавиту (парсинг Википедии)

Скрипт собирает со страницы Категория:Животные по алфавиту количество записей на каждую букву.
Результат сохраняется в файл beasts.csv.

## Задача 3: Подсчёт общего времени присутствия

Функция appearance(intervals) принимает словарь с временными интервалами:

* lesson: [start, end]
* pupil: [in1, out1, in2, out2, ...]
* tutor: [in1, out1, in2, out2, ...]


## Технологический стек
- Python 3.12
- Для задачи 2 — requests, beautifulsoup4

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone git@github.com:dariazueva/tetrika-junior.git
```

```bash
cd tetrika-junior
```

Cоздать и активировать виртуальное окружение:

```bash
python -m venv venv
```

* Если у вас Linux/macOS

    ```bash
    source venv/bin/activate
    ```

* Если у вас windows

    ```bash
    source venv/Scripts/activate
    ```

```bash
python -m pip install --upgrade pip
```

Установите необходимые зависимости:

```bash
pip install -r requirements.txt

```

Все задачи можно запускать по отдельности, как самостоятельные модули.

Через терминал:

```bash
python task1/solution.py
python task2/solution.py
python task3/solution.py
```

## Автор
Зуева Дарья Дмитриевна
Github https://github.com/dariazueva/
# Project_2 — Aircraft Tracker

Учебный проект (курсовая работа) по объектно-ориентированному программированию на Python.
Программа собирает данные о самолётах, находящихся в воздушном пространстве выбранной страны,
используя API **nominatim.openstreetmap.org** и **opensky-network.org**.

## Классы

### `BaseAPI` (абстрактный)

- `__init__(url)` — сохраняет базовый URL API.
- `get_info_about_country(country)` — абстрактный метод.
- `get_info_about_plane(country)` — абстрактный метод.

### `AeroplanesAPI(BaseAPI)`

- Работает с двумя API: Nominatim и OpenSky.
- `get_info_about_country(country)` — возвращает `boundingbox` страны.
- `get_info_about_plane(country)` — возвращает список самолётов (сырые данные).

### `Aeroplane`

- Атрибуты: `callsign`, `origin_country`, `velocity`, `baro_altitude`.
- Валидация: `None` → `"Unknown"` для строк, `None` → `0.0` для чисел.
- `__str__` — читаемое представление.
- `__lt__`, `__gt__` — сравнение по скорости.
- `__le__`, `__ge__` — сравнение по высоте.
- `cast_to_object_list(data)` — класс-метод, превращает список списков в список объектов.

### `BaseSaver` (абстрактный)

- `add_aeroplane(aeroplane)` — абстрактный метод.
- `get_aeroplanes(criteria)` — абстрактный метод.
- `delete_aeroplane(aeroplane)` — абстрактный метод.

### `JSONSaver(BaseSaver)`

- `add_aeroplane(aeroplane)` — добавляет самолёт в JSON-файл.
- `get_aeroplanes(criteria)` — возвращает самолёты по критериям (словарь).
- `delete_aeroplane(aeroplane)` — удаляет самолёт из JSON-файла.

Покрытие тестами 71%
Name                   Stmts   Miss  Cover
------------------------------------------
src\Aeroplane.py          40      0   100%
src\AeroplanesAPI.py      29     23    21%
src\JSONSaver.py          49     12    76%
src\Saver.py              11      3    73%
src\__init__.py            0      0   100%
src\base_api.py           10      3    70%
------------------------------------------
TOTAL                    139     41    71%


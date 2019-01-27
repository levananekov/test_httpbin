# Тестовое задание для Тинькофф
1. Написать и автоматизировать тест-кейсы для нескольких endpoint'ов https://httpbin.org/
/headers
/status/:code
/redirect/:n

Требования к тестам :
* Запуск тестов должен осуществляться средствами pytest (https://docs.pytest.org/en/latest/);
* Все запросы на сервер и ответы должны быть залоггированы
(https://docs.python.org/3/library/logging.html).
Ограничений в других библиотеках нет - любые сторонние библиотеки, плагины для pytest'а можно
использовать по своему усмотрению.
Логирование помимо запросов-ответов тоже по своему усмотрению.

Плюсами будут:
* Возможность собирать allure отчёт (allure-pytest-adaptor или allure-pytest). Отдельный плюс за отчёт
с логами.
* Возможность настраивать глобальное логгирование при запуске тестов (например, с помощью
https://docs.python.org/3/library/logging.config.html#configuration-dictionary-schema).
* Возможность собрать документацию по автотестам.


# Подготовка к запуску:
1. Установка зависимостей:
   `pip3 install -r requirements.txt` 

# Как использовать:
2. Запуск на *nix:
```
$ python3 -m pytest -n 4 test_*.py --alluredir reports
======================================= test session starts ========================================
platform darwin -- Python 3.7.2, pytest-4.1.1, py-1.7.0, pluggy-0.8.1
rootdir: /Users/levananenkov/test_httpbin, inifile:
plugins: xdist-1.26.0, forked-1.0.1, allure-pytest-2.5.4
gw0 [72] / gw1 [72] / gw2 [72] / gw3 [72]
........................................................................                     [100%]
==================================== 72 passed in 16.00 seconds ====================================
```

# Генерация отчета:
3. Запуск на *nix :
```
$ allure serve reports 
```

# Test Task

Проет представляет из себя решение тестового задания

## Starting
Предварительная настройка
```
Установлен python3.8
Установлен pip
Установлен пакет virtualenv
Создано виртуальное окружение
```
Установка необходимых зависимостей ```pip install -r requirements.txt```


## Usage
1. Запуск тестов осуществляется через терминал при помощи команды из корня проекта:
```bash
python -m pytest --tb=short -q [--html <имя файла>.html]
```

2. Запуск скрипта для создания базы из корня проекта
```bash
cd src
python create_db.py [-h]
```

3. Запуск скрипта для заполнения базы из корня проекта
```bash
cd src
python fill_db.py [-h]
```


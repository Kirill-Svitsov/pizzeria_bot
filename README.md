[![GitHub](https://img.shields.io/badge/GitHub-Kirill--Svitsov-blue)](https://github.com/Kirill-Svitsov)
# PizzaBot
[![Telegram Badge](https://img.shields.io/badge/-svitsov-blue?style=flat&logo=Telegram&logoColor=white)](https://t.me/Pizza_SvitsovBot)

## Description
Проект сделан с целью обучения в создании Telegram ботов. В качестве идеи принят бот, позволяющий формировать заказы в пиццерии.


## Technologies

- Python 3.11
- aiogram==3.4.1
- asyncpg==0.29.0
- pydantic==2.5.3
- SQLAlchemy==2.0.29

## Запуск проекта в режиме разработки

- Установите и активируйте виртуальное окружение.
- Установите зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
- Создайте файл .env и разместите в нем TOKEN=токен_вашего_бота
- Токен бота вы можете получить https://t.me/BotFather
- После этого вы можете запустить приложение
```
python3 app.py
```

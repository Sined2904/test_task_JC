# test_task_JC

### Описание
Тестовое задание для JavaCode. Приложение позволяет увидеть баланс конкретного кошелька, зачислить сумму или списать ее

### Технологии
asgiref
Django
djangorestframework
gunicorn
packaging
psycopg2-binary
python-dotenv
sqlparse
typing_extensions
tzdata

### Запуск проекта в dev-режиме
- Заполните файл .env
- В корневой папке проекта выполните команду:
```
docker compose up 
```

### Описание переменных окружения
SECRET_KEY - ключ проекта
DEBUG - статус режима дебаг
POSTGRES_DB - название БД
POSTGRES_USER - имя пользователя БД
POSTGRES_PASSWORD - пароль пользователя БД
DB_NAME - название БД
DB_HOST - адрес БД
DB_PORT - порт БД
OPERATIONS_OF_DEPOSIT - разрешенные операции зачисления
OPERATIONS_OF_WITHDRAW - разрешенные операции списания
ALLOWED_HOSTS - разрешенные хосты
LOCAL_DB - режим БД. При локальной работе используется Sqlite3, в противном случае PostgreSQL



### Авторы
Пиневич Денис

Github - Sined2904
Den2904@yandex.ru
TG - @PinevichD
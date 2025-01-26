# Habit_Tracker_Coursework - Трекер полезных привычек

## Описание проекта

Проект представляет собой REST API сервис для отслеживания полезных привычек. Пользователи могут создавать, отслеживать и делиться своими привычками, получать уведомления через Telegram.
Приложение доступно по IP адресу: http://51.250.38.97:8000/ 
## Функциональность

- Регистрация и авторизация пользователей
- CRUD операции с привычками
- Публичные и приватные привычки
- Интеграция с Telegram для уведомлений
- Отложенные задачи через Celery
- Валидация данных привычек
- Пагинация (5 привычек на страницу)
- API документация (Swagger/ReDoc)

## Технологии

- Python 3.10+
- Django 5.1
- Django REST Framework
- PostgreSQL
- Celery
- Redis
- Simple JWT
- Swagger/drf-yasg
- Docker & Docker Compose
- Nginx


## Установка и запуск

### Предварительные требования

- PostgreSQL
- Redis
- Docker
- Docker Compose

### Установка

1. Установить Poetry:
    ```bash
    pip install poetry
    ```
2. Установить зависимости и создать виртуальное окружение:
    ```bash
    poetry install
    ```
3. Активировать виртуальное окружение:
    ```bash
    poetry shell
    ```
4. Создать файл `.env` на основе `.env_template` и заполнить необходимые переменные окружения.

5. Выполнить миграции:
    ```bash
    python manage.py migrate
    ```

### Установка Redis

1. Установите Redis:
   - На macOS: используйте Homebrew
     ```sh
     brew install redis
     ```
   - На Ubuntu/Debian:
     ```sh
     sudo apt update
     sudo apt install redis-server
     ```
   - На Windows: скачайте и установите Redis с официального сайта или используйте WSL (Windows Subsystem for Linux).

2. Запустите Redis сервер:
   - На macOS и Linux:
     ```sh
     redis-server
     ```
   - На Windows:
     Запустите `redis-server.exe` из установленной директории.

3. Проверьте, что Redis сервер запущен:
   - Выполните команду:
     ```sh
     redis-cli ping
     ```
   - Если сервер работает, вы получите ответ `PONG`.

4. Настройте Redis сервер (опционально):
   - Откройте файл конфигурации `redis.conf` и внесите необходимые изменения.

### Локальная разработка

1. Клонировать репозиторий:

   ```bash
   git clone https://github.com/Godemd/Habit_Tracker_Coursework.git
   cd Mahiru_Habits_Coursework
   ```

2. Создать файл `.env` на основе `.env_template`

   ```bash
   cp .env.template .env
   ```

   Заполнить необходимые переменные окружения в файле .env

3. Собрать и запустить контейнеры:

   ```bash
   docker-compose up -d --build
   ```

4. Проект будет доступен по адресу: http://localhost:8000

### Остановка проекта

```bash
docker-compose down
```
## Настройка CI/CD

### GitHub Actions

1. Добавьте следующие секреты в настройки GitHub репозитория:

   - `SERVER_HOST` - IP-адрес вашего сервера
   - `SERVER_USER` - Имя пользователя на сервере
   - `SSH_PRIVATE_KEY` - SSH-ключ для доступа к серверу

2. При пуше в ветку main автоматически запускаются:
   - Тесты
   - Линтинг кода
   - Сборка Docker образов
   - Деплой на сервер

### Настройка сервера

1. Установите Docker:

   ```bash
   sudo apt update
   sudo apt install docker.io
   ```

2. Установите Docker Compose:

   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/download/v2.24.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

3. Настройте SSH доступ для GitHub Actions

## Функциональность

- Регистрация и авторизация пользователей
- CRUD операции с привычками
- Публичные и приватные привычки
- Интеграция с Telegram для уведомлений
- Отложенные задачи через Celery
- Валидация данных привычек
- Пагинация (5 привычек на страницу)
- API документация (Swagger/ReDoc)

## Тестирование

Запуск тестов в Docker:

```bash
docker-compose exec web python manage.py test
```
### Запуск

1. Запустить Redis сервер.

2. Запустить Celery:
    ```bash
    celery -A проект worker -l info
    ```
3. Запустить Django сервер:
    ```bash
    python manage.py runserver
    ```

## API Endpoints

- `POST /api/register/` - Регистрация пользователя
- `POST /api/token/` - Получение JWT токена
- `GET /api/habits/` - Список привычек авторизованного пользователя
- `POST /api/habits/` - Создание новой привычки
- `GET /api/habits/public/` - Список публичных привычек
- `GET /api/habits/<int:pk>/` - Получение деталей конкретной привычки
- `PUT /api/habits/<int:pk>/` - Обновление конкретной привычки
- `PATCH /api/habits/<int:pk>/` - Частичное обновление конкретной привычки
- `DELETE /api/habits/<int:pk>/` - Удаление конкретной привычки
- `/swagger/` - Swagger документация
- `/redoc/` - ReDoc документация


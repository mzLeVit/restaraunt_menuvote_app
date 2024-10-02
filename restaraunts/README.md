# Restaurant Menu Vote App

Restaurant Menu Vote App — це система для голосування за обід серед співробітників, яка складається з бекенду на основі Django + DRF та фронтенду на React. Користувачі можуть автентифікуватися, переглядати меню, голосувати за улюблену страву та переглядати результати голосування.

## Особливості

- Автентифікація користувачів за допомогою JWT.
- Створення ресторанів та завантаження меню.
- Голосування за обіди.
- Перегляд результатів голосування.
- Можливість зміни голосу.
- Фронтенд на React з підтримкою Redux або Context API.

## Технології

- **Backend**: Django, Django REST Framework, PostgreSQL
- **Frontend**: React, Redux / Context API
- **Docker**: Для контейнеризації та запуску сервісів
- **Тести**: PyTest для бекенду

## Вимоги

- Docker
- Docker Compose

## Як запустити проект локально

### 1. Клонування репозиторію

Клонувати репозиторій до вашого локального середовища:

```bash
git clone https://github.com/mzLeVit/restaraunt_menuvote_app.git
cd restaraunt_menuvote_app
```
### 2. Налаштування середовища
Створіть файл .env в кореневій директорії проекту з наступними змінними оточення:
```
SECRET_KEY=ваш_секретний_ключ
DEBUG=True
DB_NAME=restaurant_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```
### 3. Запуск контейнерів з Docker
Увімкніть Docker і виконайте наступну команду для запуску контейнерів:

```docker-compose up --build```
Це запустить всі необхідні сервіси, включаючи бекенд, фронтенд та базу даних PostgreSQL.

### 4. Міграція бази даних
В іншому терміналі виконайте команду для застосування міграцій до бази даних:

```

docker-compose exec backend python manage.py migrate
```
### 5. Створення суперкористувача
Щоб створити адміністратора для доступу до адмін-панелі Django, виконайте:

```
docker-compose exec backend python manage.py createsuperuser
```
Дотримуйтесь інструкцій для створення облікового запису адміністратора.

### 6. Доступ до системи
Бекенд буде доступний за адресою: http://localhost:8000/api/
Фронтенд буде доступний за адресою: http://localhost:3000/
### 7. Тестування
Для запуску тестів використовуйте наступну команду:

```
docker-compose exec backend pytest
```
### 8. Зупинка контейнерів
Щоб зупинити роботу контейнерів, скористайтеся командою:

```
docker-compose down
```
Додаткові команди
Запуск міграцій:
```
docker-compose exec backend python manage.py migrate
```
Завантаження статики:
```
docker-compose exec backend python manage.py collectstatic
```

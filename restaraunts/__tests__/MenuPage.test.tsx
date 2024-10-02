# Lunch Voting App

## Backend Setup

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Run Docker Compose:
    ```bash
    docker-compose up --build
    ```

3. Apply migrations:
    ```bash
    python manage.py migrate
    ```

4. Run server:
    ```bash
    python manage.py runserver
    ```

## Frontend Setup

1. Install dependencies:
    ```bash
    npm install
    ```

2. Run the app:
    ```bash
    npm start
    ```

## Running Tests

- Backend: `pytest`
- Frontend: `npm test`

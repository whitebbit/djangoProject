# Django с Celery для отправки SMS

Этот проект использует Celery для асинхронной отправки SMS через Django с использованием Twilio (или другого провайдера).

## Установка

1. Склонируйте репозиторий на свой компьютер.
2. Создайте виртуальное окружение и активируйте его:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Для UNIX или MacOS
    venv\Scripts\activate  # Для Windows
    ```

3. Установите необходимые пакеты:

    ```bash
    pip install -r requirements.txt
    ```

## Настройка

1. Добавьте необходимые переменные окружения для конфиденциальных данных, таких как Twilio SID, токен и т. д.

   ```bash
    export TWILIO_ACCOUNT_SID="your_account_sid"
    export TWILIO_AUTH_TOKEN="your_auth_token"
    export TWILIO_NUMBER="your_number"
    ```
   
## Запуск RabbitMQ, Celery, и сервера Django

1. Запустите RabbitMQ:

    ```bash
    docker run -d -p 5672:5672 rabbitmq
    ```

2. Запустите Celery worker:

    ```bash
    celery -A your_project worker -l info
    ```

3. Запустите веб-сервер Django:

    ```bash
    python manage.py runserver
    ```


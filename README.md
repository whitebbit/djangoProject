# Django Blog Caching

Этот проект реализует механизм кэширования для блога в Django с целью улучшения времени загрузки страниц.

## Установка

1. Склонируйте репозиторий на свой компьютер.
    ```bash
    git clone https://github.com/whitebbit/djangoProject.git
    cd djangoProject
    ```
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

1. Применение миграций:

   ```bash
    python manage.py migrate
    ```
2. Заполнение базы данных блогом:

    ```bash
    python manage.py populate_blog <count>
    ```
   
## Запуск RabbitMQ, Celery, и сервера Django

1. Запустите Redis:

    ```bash
    docker run -p 6379:6379 redis
    ```
2. Запустите веб-сервер Django:

    ```bash
    python manage.py runserver
    ```
3. Откройте браузер и перейдите по адресу http://localhost:8000/blog/1/ (или другому id блога) для просмотра блогов.


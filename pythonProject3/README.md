Установка и настройка
1. Клонирование репозитория:

   git clone https://github.com/your_username/your_project.git
   cd your_project
2. Установка зависимостей:
   Создайте и активируйте виртуальное окружение (опционально):
   python -m venv venv
   Для Windows:
   venv\Scripts\activate
   Для Linux/macOS:
   source venv/bin/activate
   pip install -r requirements.txt
3. Настройка базы данных:
   - Установите PostgreSQL и убедитесь, что сервер запущен.
   - Создайте новую базу данных для этого приложения.

4. Конфигурация приложения:
   Создайте файл `config.py` в корне проекта и добавьте следующие настройки:
python
   config.py

   class Config:
       SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/dbname'
       SQLALCHEMY_TRACK_MODIFICATIONS = False
5. Инициализация базы данных:
   В консоли выполните следующие команды для инициализации базы данных:
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   Эти команды создадут необходимые таблицы в базе данных PostgreSQL.
Запуск

1. Запуск сервера Flask:
   В корневой директории проекта выполните:
   python app.py
   Приложение будет запущено на `http://127.0.0.1:5000/`.
2. Проверка работоспособности:
   - Откройте браузер и перейдите по URL `http://127.0.0.1:5000/` для проверки основной страницы (должен отобразиться "Hello, World!").
   - Для проверки API, используйте URL вида `http://127.0.0.1:5000/api/logs?start_date=2024-06-10&end_date=2024-06-12&ip=192.168.1.1`, чтобы получить данные логов

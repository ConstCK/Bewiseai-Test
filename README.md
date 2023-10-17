
Скопируйте проект к себе на ПК при помощи: git clone https://github.com/ConstCK/Bewiseai-Test.git
Создайте файл .env в каталоге проекта и пропишите в нем свои значения по примеру .env.example

Примечание:
Можно использовать:
SECRET_KEY = Ключ для Django можно сгенерировать по пути https://djecrety.ir/
DB_NAME = quizdb
USER_NAME = postgres
PASSWORD = admin

Запустите Docker Desktop для дальнейшей работы!
Выполните команду в терминале из каталога проекта: docker-compose up

EndPoints:
http://127.0.0.1:8000/api/ - post запрос с body {"number": Ваше число}
Примечание:
используйте Postman для запросов

http://127.0.0.1:8888/ - доступ к adminer (управление БД)
Примечание:
имя пользователя, пароль и бд берем из .env, сервер - postgres, движок - PostgreSQL






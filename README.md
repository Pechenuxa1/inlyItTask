# inlyItTask

Сначала запускается база данных через "docker compose up -d", дальше запускается сервис через "uvicorn main:app".
Чтобы посмотреть содержимое таблицы вводим docker exec -it {имя контейнера в "docker ps"} psql -U user testdb и дальше "SELECT * FROM user_goods".

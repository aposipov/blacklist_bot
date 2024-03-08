
all:
		@echo "build and run"

build:
		docker build -t blacklist_bot .

run:	build
		docker run --name blacklist_cont -v $(PWD)/core_bot/data:/bot/data \
		-d --restart=unless-stopped blacklist_bot

clear:
		docker stop blacklist_cont
		docker container rm blacklist_cont
		docker image rm blacklist_bot:latest

db_init:
		python3 core_bot/db/init_db.py

db_drop:
		sqlite3 core_bot/data/dev_blacklist.db "DROP TABLE bl_users;"

db_users:
		sqlite3 core_bot/data/dev_blacklist.db "SELECT * FROM bl_users;"

db_drivers:
		sqlite3 core_bot/data/dev_blacklist.db "SELECT * FROM bl_drivers;"

start:
		python3 core_bot/main.py

test:
		pytest -v


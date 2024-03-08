
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

db_init:
		python3.11 core_bot/db/init_db.py

start:
		python3.11 core_bot/main.py

test:
		pytest -v


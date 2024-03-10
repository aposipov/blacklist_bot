import sqlite3

db_path = 'core_bot/data/dev_blacklist.db'


def init_db():
	db = None
	try:
		db = sqlite3.connect(db_path)
		c = db.cursor()
		c.execute("CREATE TABLE IF NOT EXISTS bl_users ("
		          "id INTEGER PRIMARY KEY AUTOINCREMENT,"
		          "tg_id INTEGER UNIQUE NOT NULL,"
		          "accept INTEGER DEFAULT 0,"
		          "username VARCHAR(250),"
		          "fullname VARCHAR(250),"
		          "phone VARCHAR(12),"
		          "city VARCHAR(250),"
		          "about TEXT,"
		          "lang VARCHAR(10),"
		          "premium INTEGER DEFAULT 0,"
		          "date TIMESTAMP,"
		          "count_requests INTEGER,"
		          "count_blacklist_add INTEGER,"
		          "invite_code VARCHAR(8) UNIQUE DEFAULT (SUBSTR(HEX(RANDOM()), 1, 8)),"
		          "invitation_from VARCHAR(8) DEFAULT X)")

		c.execute("CREATE TABLE IF NOT EXISTS bl_drivers ("
		          "id INTEGER PRIMARY KEY AUTOINCREMENT,"
		          "landlord_id INTEGER NOT NULL REFERENCES bl_users (tg_id),"
		          "driver_id INTEGER NOT NULL,"
		          "blacklist INTEGER DEFAULT 0,"
		          "tracking INTEGER DEFAULT 0,"
		          "fullname VARCHAR(250),"
		          "birthday VARCHAR(10),"
		          "comment TEXT,"
		          "rating INTEGER DEFAULT 0,"
		          "passport INTEGER UNIQUE,"
		          "phone VARCHAR(12),"
		          "img_driver_id VARCHAR(250),"
		          "img_other VARCHAR(250),"
		          "date TIMESTAMP)")
	except Exception as e:
		print(f'INIT DB ERROR! {e}')
	db.commit()
	db.close()


init_db()
print("DB create!")

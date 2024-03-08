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
		          "username VARCHAR(250),"
		          "fullname VARCHAR(250),"
		          "phone VARCHAR(12),"
		          "accept INTEGER DEFAULT 0,"
		          "city VARCHAR(250),"
		          "about TEXT,"
		          "lang VARCHAR(10),"
		          "premium INTEGER DEFAULT 0,"
		          "date TIMESTAMP)")

		c.execute("CREATE TABLE IF NOT EXISTS bl_drivers ("
		          "id INTEGER PRIMARY KEY AUTOINCREMENT,"
		          "driver_id INTEGER UNIQUE NOT NULL,"
		          "fullname VARCHAR(250),"
		          "birthday VARCHAR(10),"
		          "comment TEXT,"
		          "rating INTEGER DEFAULT 0,"
		          "passport INTEGER UNIQUE,"
		          "phone VARCHAR(12),"
		          "img_path VARCHAR(250),"
		          "date TIMESTAMP)")
	except Exception as e:
		print(f'INIT DB ERROR! {e}')
	db.commit()
	db.close()


init_db()
print("DB create!")

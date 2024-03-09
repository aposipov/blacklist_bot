import sqlite3

db_path = 'data/dev_blacklist.db'


def checking_accept(user_id: int):
	try:
		db = sqlite3.connect(db_path)
		c = db.cursor()
		c.execute("SELECT accept FROM bl_users WHERE tg_id = ?", (user_id,))
		result = c.fetchone()
		if result:
			return result[0] == 1
		else:
			return False
	except sqlite3.Error as e:
		print(f'add_phone ERROR! {e}')
	finally:
		if db:
			db.close()

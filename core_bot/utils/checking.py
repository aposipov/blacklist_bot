import sqlite3
from init_bot import DB_PATH

db_path = DB_PATH


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
		print(f'checking_accept ERROR! {e}')
	finally:
		if db:
			db.close()


def checking_invitation(user_id: int):
	try:
		db = sqlite3.connect(db_path)
		c = db.cursor()
		c.execute("SELECT invitation_from FROM bl_users WHERE tg_id = ?", (user_id,))
		result = c.fetchone()
		if result:
			return result[0] == 'X'
		else:
			return False
	except sqlite3.Error as e:
		print(f'checking_invitation ERROR! {e}')
	finally:
		if db:
			db.close()

import sqlite3
from init_bot import DB_PATH
from aiogram.types import Message

# id|driver_id|fullname|birthday|comment|rating|passport|phone|img_path|date
db_path = DB_PATH


def add_driver_db(profile: dict, tg_id: int):
	try:
		db = sqlite3.connect(db_path)
		c = db.cursor()
		c.execute(
			"INSERT INTO bl_drivers (landlord_id, driver_id, fullname, birthday) "
			"VALUES (?,?,?,?)",
			(tg_id, profile['id_driver'], profile['name'], profile['bd_driver'],))
		db.commit()
	except sqlite3.Error as e:
		print(f'add_driver_db ERROR! {e}')
	finally:
		if db:
			db.close()


def search_driver_db(profile: dict):
	try:
		db = sqlite3.connect(db_path)
		c = db.cursor()
		c.execute(
			"SELECT driver_id, blacklist, tracking, fullname, birthday, comment "
			"FROM bl_drivers "
			"WHERE blacklist = ? AND fullname = ? AND birthday = ? "
			"OR blacklist = ? AND driver_id = ?",
			(1, profile['name'], profile['bd_driver'], 1, profile['id_driver'],))
		result = c.fetchall()
		if result:
			return result
	except sqlite3.Error as e:
		print(f'search_driver_db ERROR! {e}')
	finally:
		if db:
			db.close()


def add_driver_bl(profile: dict, tg_id: int):
	try:
		db = sqlite3.connect(db_path)
		c = db.cursor()
		c.execute(
			"INSERT INTO bl_drivers (landlord_id, driver_id, "
			"fullname, birthday, comment, blacklist) "
			"VALUES (?,?,?,?,?,?)",
			(tg_id, profile['driverid'], profile['fullname'], profile['bd'],
			 profile['comment'], 1,))
		db.commit()
	except sqlite3.Error as e:
		print(f'add_driver_bl ERROR! {e}')
	finally:
		if db:
			db.close()

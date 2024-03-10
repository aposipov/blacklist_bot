import sqlite3
from aiogram.types import Message

# id|driver_id|fullname|birthday|comment|rating|passport|phone|img_path|date
db_path = 'data/dev_blacklist.db'


def add_driver_db(profile, tg_id):
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


def search_driver():
	pass

import csv
import sqlite3

path_to_file = 'core_bot/data/mock_data.csv'
db_path = 'core_bot/data/dev_blacklist.db'


def db_add(row):
	tg_id: int = row[0]
	driver_id: int = row[1]
	bl: int = row[2]
	track: int = row[3]
	full_name: str = row[4]
	bd: str = row[5]
	comment: str = row[6]
	try:
		db = sqlite3.connect(db_path)
		c = db.cursor()
		c.execute("INSERT INTO bl_drivers "
		          "(landlord_id, driver_id, blacklist, tracking, fullname, birthday, comment)"
		          "VALUES (?,?,?,?,?,?,?)",
		          (tg_id, driver_id, bl, track, full_name, bd, comment))
		db.commit()
		db.close()
		print(f'Driver {full_name} added to DB!')
	except sqlite3.Error as e:
		print(f'add_data ERROR! {e}')


def read_file():
	try:
		with open(path_to_file, 'r', encoding='utf-8') as f:
			reader = csv.reader(f, delimiter=';')
			for row in reader:
				if row and row[0].isdigit():
					db_add(row)
				else:
					continue
	except Exception as e:
		print(f'ERROR {e}')


read_file()
print(" Driver upload OK!")

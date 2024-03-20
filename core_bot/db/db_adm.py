import sqlite3
from init_bot import DB_PATH
# from aiogram.types import Message

db_path = DB_PATH


def accept_user(user: int):
    try:
        db = sqlite3.connect(db_path)
        c = db.cursor()
        c.execute("UPDATE bl_users SET accept = ? WHERE tg_id = ?", (1, user))
        db.commit()
    except sqlite3.Error as e:
        print(f'add_phone ERROR! {e}')
    finally:
        if db:
            db.close()


def decline_user(user: int):
    try:
        db = sqlite3.connect(db_path)
        c = db.cursor()
        c.execute("UPDATE bl_users SET accept = ? WHERE tg_id = ?", (0, user))
        db.commit()
    except sqlite3.Error as e:
        print(f'add_phone ERROR! {e}')
    finally:
        if db:
            db.close()

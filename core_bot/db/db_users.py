import sqlite3
from aiogram.types import Message

db_path = 'data/dev_blacklist.db'

# id|tg_id|username|fullname|phone|accept|city|about|lang|premium|date


def add_user_db(message: Message):
    user_id: int = message.from_user.id
    if message.from_user.username is None:
        username: str = 'null'
    else:
        username = '@' + message.from_user.username
    fullname: str = message.from_user.full_name
    lang: str = message.from_user.language_code
    premium: bool = message.from_user.is_premium
    date = message.date
    db = None
    try:
        db = sqlite3.connect(db_path)
        c = db.cursor()
        # c.execute("INSERT INTO bl_users VALUES (NULL,?,?,?,NULL,NULL,NULL,NULL,?,?,?)",
        #           (user_id, username, full_name, lang, premium, date))
        c.execute("INSERT INTO bl_users (tg_id, username, fullname, lang, premium, date) "
                  "VALUES (?,?,?,?,?,?)",
                  (user_id, username, fullname, lang, premium, date,))
        db.commit()
        print(f'User {user_id} added to DB!')
    except sqlite3.Error as e:
        print(f'add_data ERROR! {e}')
    finally:
        if db:
            db.close()


def add_phone(phone: str, user: int):
    try:
        db = sqlite3.connect(db_path)
        c = db.cursor()
        c.execute("UPDATE bl_users SET phone = ? WHERE tg_id = ?", (phone, user))
        db.commit()
    except sqlite3.Error as e:
        print(f'add_phone ERROR! {e}')
    finally:
        if db:
            db.close()


def add_about_user(text: str, user: int):
    try:
        db = sqlite3.connect(db_path)
        c = db.cursor()
        # c.execute("INSERT INTO bl_users (tg_id, about) VALUES (?,?)", (text,))
        c.execute("UPDATE bl_users SET about = ? WHERE tg_id = ?", (text, user))
        db.commit()
    except sqlite3.Error as e:
        print(f'add_about_user ERROR! {e}')
    finally:
        if db:
            db.close()


def add_icode(code: str, user: int):
    try:
        db = sqlite3.connect(db_path)
        c = db.cursor()
        c.execute("UPDATE bl_users SET invitation_from = ? WHERE tg_id = ?",
                  (code, user))
        db.commit()
    except sqlite3.Error as e:
        print(f'add_icode ERROR! {e}')
    finally:
        if db:
            db.close()


def get_icode(userid: int) -> str:
    try:
        db = sqlite3.connect(db_path)
        c = db.cursor()
        c.execute("SELECT invite_code FROM bl_users WHERE tg_id = ?", (userid,))
        result = c.fetchone()
        if result:
            return result[0]
    except sqlite3.Error as e:
        print(f'get_icode ERROR! {e}')
    finally:
        if db:
            db.close()

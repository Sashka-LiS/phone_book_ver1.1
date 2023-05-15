import sqlite3 as sq


def get_db():
    """Возвращает контакт к БД"""
    connection_db = sq.connect("phone_book.db")
    return connection_db

def create_db():
    """Создание БД"""
    with sq.connect('phone_book.db') as phone_book:
        cursor = phone_book.cursor()

        query = ('''
                CREATE TABLE IF NOT EXISTS contacts
                (
                    id_contact INTEGER PRIMARY KEY,
                    surname TEXT,
                    name TEXT NOT NULL,
                    father_name TEXT,
                    email TEXT
                );

                CREATE TABLE IF NOT EXISTS numbers
                (
                    id_number INTEGER PRIMARY KEY,
                    number TEXT,
                    type TEXT,
                    id_contact INTEGER,
                    FOREIGN KEY (id_contact) REFERENCES contacts (id_contact) ON DELETE CASCADE
                );
                ''')

        cursor.executescript(query)
    return True

def close_db(phone_book=get_db()):
    phone_book.close()

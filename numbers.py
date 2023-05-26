import db


class NumberRecord:
    def __init__(self, number: str, type: str, id_contact: int):
        self.number = number
        self.type = type
        self.id_contact = id_contact


def add_number(number_rec: NumberRecord):
    """Добавляет в таблицу numbers"""
    phone_book = db.get_db()
    cursor = phone_book.cursor()
    val_number = [number_rec.number, number_rec.type, number_rec.id_contact]
    cursor.execute("INSERT INTO numbers(number, type, id_contact) VALUES (?, ?, ?);", val_number)
    phone_book.commit()
    id = cursor.lastrowid
    cursor.close()
    return id

def find_numbers(id: int)-> list:
    phone_book = db.get_db()
    cursor = phone_book.cursor()
    cursor.execute("SELECT * FROM numbers WHERE id_contact = ?;", [id])
    numbers = []
    for number in cursor.fetchall():
        numbers.append(number)
    return numbers
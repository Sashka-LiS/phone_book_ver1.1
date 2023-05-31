import db
import UI

class NumberRecord:
    def __init__(self, id: int, number: str, type: str, id_contact: int):
        self.id = id
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

def find_numbers(id: int)-> list[NumberRecord]:
    phone_book = db.get_db()
    cursor = phone_book.cursor()
    cursor.execute("SELECT * FROM numbers WHERE id_contact = ?;", [id])
    numbers = []
    for number in cursor.fetchall():
        numbers.append(NumberRecord(number[0], number[1], number[2], number[3]))
    return numbers

def del_number(id_number: int):
    phone_book = db.get_db()
    cursor = phone_book.cursor()
    cursor.execute("DELETE from numbers WHERE id_number = ?;", [id_number])
    phone_book.commit()
    cursor.close()
    return True

def update_number(id_number: int, new_number: str, new_type: str):
    phone_book = db.get_db()
    cursor = phone_book.cursor()
    cursor.execute("""UPDATE numbers
                      SET number = ?, type = ?
                      WHERE id_number = ?;""", [new_number, new_type, id_number])
    phone_book.commit()
    cursor.close()

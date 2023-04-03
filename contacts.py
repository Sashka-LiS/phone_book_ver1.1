import db

class ContactRecord:
    def __init__(self, surname: str, name: str, father_name: str, email: str):
        self.surname = surname
        self.name = name
        self.father_name = father_name
        self.email = email

class NumberRecord:
    def __init__(self, number: str, type: str, id_contact: int):
        self.number = number
        self.type = type
        self.id_contact = id_contact


def add_contact(contact_rec: ContactRecord):
    """Добавляет в таблицу contacts"""
    phone_book = db.get_db()
    cursor = phone_book.cursor()
    val_contact = [contact_rec.surname, contact_rec.name, contact_rec.father_name, contact_rec.email]
    cursor.execute("INSERT INTO contacts(surname, name, father_name, email) VALUES (?, ?, ?, ?);", val_contact)
    phone_book.commit()
    id = cursor.lastrowid
    cursor.close()
    return id

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




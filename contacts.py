import db
import UI

class ContactRecord:
    def __init__(self, id: int,surname: str, name: str, father_name: str, email: str):
        self.id = id
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

def del_contact(id: int):
    phone_book = db.get_db()
    cursor = phone_book.cursor()
    val_for_del = [id]
    cursor.execute('PRAGMA foreign_keys=on')
    cursor.execute('DELETE FROM contacts WHERE id_contact = ?', val_for_del)
    phone_book.commit()
    cursor.close()
    return True

def xz_kakoe_nazvanie(query, value: str)-> list:
    phone_book = db.get_db()
    cursor = phone_book.cursor()
    list_contacts = []
    if value == None:
        cursor.execute(query)
    else:
        cursor.execute(query, value)
    for contact in cursor.fetchall():
        list_contacts.append(ContactRecord(contact[0], contact[1], contact[2], contact[3], contact[4]))
    return list_contacts

def find_contact(value=None)-> list[ContactRecord]:
    contacts = []
    if value == None:
        all_contacts = ("SELECT id_contact, surname, name, father_name, email FROM contacts;")
        contacts += xz_kakoe_nazvanie(all_contacts, value)        
        return contacts
    else:
        value = ["%" + value + "%"]
        find_surname = "SELECT id_contact, surname, name, father_name, email FROM contacts WHERE surname LIKE ?;"
        contacts += xz_kakoe_nazvanie(find_surname, value)
        find_name = "SELECT id_contact, surname, name, father_name, email FROM contacts WHERE name LIKE ?;"
        contacts += xz_kakoe_nazvanie(find_name, value)
        find_father_name = "SELECT id_contact, surname, name, father_name, email FROM contacts WHERE father_name LIKE ?;"
        contacts += xz_kakoe_nazvanie(find_father_name, value)
        find_email = "SELECT id_contact, surname, name, father_name, email FROM contacts WHERE email LIKE ?;"
        contacts += xz_kakoe_nazvanie(find_email, value)
    return contacts

def show_number_cont(id: int)-> list:
    phone_book = db.get_db()
    cursor = phone_book.cursor()
    cursor.execute("SELECT * FROM numbers WHERE id_contact = ?;", [id])
    numbers = []
    for number in cursor.fetchall():
        numbers.append(ContactRecord(None, number[1], number[2], None, None)) # использовал объект ContactRecord для отображения number и type
    return numbers 
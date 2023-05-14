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

def find_contact(val_for_search: str)-> list[ContactRecord]:
    val_for_search = ["%" + val_for_search + "%"]
    phone_book = db.get_db()
    cursor = phone_book.cursor()
    cursor.execute("SELECT id_contact, surname, name, father_name, email FROM contacts WHERE name LIKE ?;", val_for_search)
    contacts = []
    for contact in cursor.fetchall():
        contacts.append(ContactRecord(contact[0], contact[1], contact[2], contact[3], contact[4]))
    return contacts

# МОЖНО ОТФИЛЬТРОВАТЬ ПОВЬОРЯЮЩИЕСЯ ЗНАЧЕНИЯ В СПИСКЕ FILTER

# def show_book():
#     phone_book = db.get_db()
#     cursor = phone_book.cursor()
#     cursor.execute("""SELECT contacts.id_contact, contacts.surname, contacts.name, contacts.father_name, contacts.email, numbers.type, numbers.number
#                       FROM contacts, numbers
#                       WHERE contacts.id_contact = numbers.id_contact;""")
#     contacts = {}
#     for contact in cursor.fetchall():
#         contact = list(contact)
#         key = contact[0]
#         values = contact[1:]
#         if key in contacts:
#             contacts[key].extend(contacts[key])
#         if contacts[key][0:3] == contacts[key][]
#         else:
#             contacts[key] = values
            
    print(contacts)

                

        
    

# def find_number()-> list[NumberRecord]:
#     phone_book = db.get_db()
#     cursor = phone_book.cursor()
#     cursor.execute("SELECT number, type, id_contact FROM numbers;")
#     numbers = []
#     for num in cursor.fetchall():
#         numbers.append(NumberRecord(num[0], num[1], num[2]))
#     return numbers




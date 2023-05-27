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

def find_numbers(id: int)-> list:
    phone_book = db.get_db()
    cursor = phone_book.cursor()
    cursor.execute("SELECT * FROM numbers WHERE id_contact = ?;", [id])
    numbers = []
    for number in cursor.fetchall():
        numbers.append(number)
    return numbers

def del_number(id_number: int):
    phone_book = db.get_db()
    cursor = phone_book.cursor()
    cursor.execute("DELETE from numbers WHERE id_number = ?;", [id_number])
    phone_book.commit()
    cursor.close()
    return True

def number_to_menu_item(number: NumberRecord)-> UI.Menuitem:
    return UI.Menuitem(f"{number.number} {number.type}", number)

def choice_number_menu(title: str, items: list[NumberRecord]):
    menu_items = []
    for number in items:
        menu_items.append(number_to_menu_item(number))
    return UI.print_menu(title, menu_items).value.id
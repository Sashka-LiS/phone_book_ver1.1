import db
import UI
import contacts
import validation
import sys
from pprint import pprint


def get_val_for_contacts():
    """Возвращает объект с атрибутами для таблицы contacts"""
    surname = input("Surname (Press 0 to cancel)--> ")
    if surname == "0":
        return False
    name = input("Name (Press 0 to cancel)--> ")
    if name == "0":
        return False
    while not validation.is_valid_name(name):
        print("This field cannot be empty.")
        name = input("Name (Press 0 to cancel)--> ")
        if name == "0":
            return False
    father_name = input("Patronymic (Press 0 to cancel)--> ")
    if father_name == "0":
        return False
    email = input("Email (Press 0 to cancel)--> ")
    if email == "0":
        return False
    while not validation.is_valid_email(email):
        print("This email is already in the phone book.")
        email = input("Email (Press 0 to cancel)--> ")
        if email == "0":
            return False
    contact_rec = contacts.ContactRecord(None, surname, name, father_name, email)
    return contact_rec

def get_val_for_numbers(id_contact: int):
    """Возвращает объект с атрибутами для таблицы numbers"""
    number = input("Number (Press 0 to cancel)--> ")
    if number == "0":
        return False
    while not validation.is_valid_number(number):
        print("Phone number format should be +7... or 8...")
        number = input("Number (Press 0 to cancel)--> ")
        if number == "0":
            return False
    type = input("Type for number (Press 0 to cancel)--> ")
    if type == "0":
        return False
    number_rec = contacts.NumberRecord(number, type, id_contact)
    return number_rec
          
def add_contact():
    """Добавляет запись в БД"""
    print("\nAdding a new contact...")
    contact_rec = get_val_for_contacts()
    if not contact_rec:
        print("Contact not added.")
        return False
    id = contacts.add_contact(contact_rec)
    number_rec = get_val_for_numbers(id)
    if not number_rec:
        print("Number not added.")
        return False
    contacts.add_number(number_rec)
    response = None
    while response != "N":
        response = input("Add another number for this contact?(Y/N) --> ").title()
        if response == "Y":
            number_rec = get_val_for_numbers(id)
            if not number_rec:
                print("Number not added.")
                return False
            contacts.add_number(number_rec)
        else:
            response = input("\nAdd another number for this contact?(Y/N) --> ").title()
    print("\nThe contact is saved in the phone book.") 
    return True

def on_exit():
    """Закрывает БД и выходит из программы"""
    db.close_db()
    print("\nHave a nice day!=)")
    sys.exit()

def del_contact():
    name = input("Search by name --> ")
    list_contacts = contacts.find_contact(name)
    if not list_contacts:
        print("\nContact not found.")
        return None
    del_menu = []
    for contact in list_contacts:
        del_menu.append(UI.Menuitem(contact.name, contact))
    del_menu.append(UI.Menuitem("Cancel", None))
    selected = UI.print_menu("_CHOOSE CONTACT TO DELETE_", del_menu)
    if selected.value == None:
        return None
    contacts.del_contact(selected.value.id)
    print()
    print(f"Contact {selected.value.name} deleted.")

def show_book():
    all_contacts = contacts.find_contact()
    show_book_menu = []
    for contact in all_contacts:
        show_book_menu.append(UI.Menuitem(f"{contact.surname} {contact.name} {contact.father_name} {contact.email}", contact))
    show_book_menu.append(UI.Menuitem("Cancel", None))
    selected = UI.print_menu("_____ALL CONTACTS_____", show_book_menu)
    if selected.value == None:
        return None
    pprint(contacts.show_book(selected.value.id))    

main_menu = [UI.Menuitem("Add new contact", add_contact),
             UI.Menuitem("Delete contact", del_contact),
             UI.Menuitem("Show book", show_book),
             UI.Menuitem("Exit", on_exit)]

def main():
    db.create_db()
    while True:
        UI.print_menu("______MENU______", main_menu).value()
        
    

if __name__ == "__main__":
    main()

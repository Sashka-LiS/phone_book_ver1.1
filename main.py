import db
import UI
import contacts
import validation
import sys
#Реализовать удаление контакта. Посмотреть старый вариант и сделать лучше.

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
    contact_rec = contacts.ContactRecord(surname, name, father_name, email)
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

def add_additional_number(id_contact: int):
    """Добавляет допномер для одного контакта"""
    while True:
        answer = input("Add another number to this contact?(Y/N)--> ").title()
        if answer == "Y":
            number_rec = get_val_for_numbers(id_contact)
            contacts.add_number(number_rec)
            print("\nThe number has been added.")
        elif answer == "N":
            print(f"\nContact added. Contact ID: {id_contact}")
            break
        else:
            print("Try again(Y/N)--> ")
            
def add_contact():

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
    add_additional_number(id)

def on_exit():
    """Закрывает БД и выходит из программы"""
    db.close_db()
    print("\nHave a nice day!=)")
    sys.exit()
    
def del_contact():
    pass

main_menu = [UI.Menuitem("Add new contact", add_contact),
             UI.Menuitem("Delete contact", del_contact),
             UI.Menuitem("Exit", on_exit)]

def main():
    db.create_db()
    while True:
        UI.print_menu("______MENU______", main_menu).handler()
        
    

if __name__ == "__main__":
    main()
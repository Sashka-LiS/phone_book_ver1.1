import db
import UI
import contacts
import validation
import sys
import numbers


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
    number_rec = numbers.NumberRecord(None, number, type, id_contact)
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
    numbers.add_number(number_rec)
    response = None
    while response != "N":
        response = input("Add another number for this contact?(Y/N) --> ").title()
        if response == "Y":
            number_rec = get_val_for_numbers(id)
            if not number_rec:
                print("Number not added.")
                return False
            numbers.add_number(number_rec)
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

def del_number(id_number):
    numbers.del_number(id_number)
    print(f"Number {id_number} deleted.")

def update_number(id_number):
    get_val_for_numbers
    # new_number = input("\nNew number(Press 0 to cancel)--> ")
    # if new_number == "0":
    #     return None
    # while not validation.is_valid_number(new_number):
    #     print("Phone number format should be +7... or 8...")
    #     number = input("Number (Press 0 to cancel)--> ")
    #     if number == "0":
    #         return False
    # new_type = input("New type(Press 0 to cancel)--> ")
    # if new_type == "0":
    #     return None
    numbers.update_number(id_number, new_number, new_type)
    print(f"Number {id_number} updated")

def show_contact_menu(value=None):
    cont = contacts.find_contact(value)
    choice = choice_contact_menu("_____CONTACTS_____", cont)
    if choice == None:
        return None
    contact_number_list(choice.id)

def choice_contact_menu(title: str, items: list[contacts.ContactRecord])-> int:
    menu_items = []
    for contact in items:
        menu_items.append(UI.Menuitem(f"{contact.surname} {contact.name} {contact.father_name} {contact.email}", contact))
    menu_items.append(UI.Menuitem("Cancel", None))
    choice = UI.print_menu(title, menu_items).value
    return choice

def contact_number_list(id_contact:int):
    numb = numbers.find_numbers(id_contact)
    choice = choice_number_menu("_____NUMBERS_____", numb)
    if choice == None:
        return None
    contact_number_actions(choice.id)

def choice_number_menu(title: str, items: list[numbers.NumberRecord]):
    menu_items = []
    for number in items:
        menu_items.append(UI.Menuitem(f"{number.number} {number.type}", number))
    menu_items.append(UI.Menuitem("Cancel", None))
    choice = UI.print_menu(title, menu_items).value
    return choice

def contact_number_actions(id_number):
    action_menu = [UI.Menuitem("Delete number", lambda: del_number(id_number)),
                   UI.Menuitem("Update number", lambda: update_number(id_number)),
                   UI.Menuitem("Cancel", None)]
    action = UI.print_menu("_____ACTION FOR NUMBER_____", action_menu).value
    if action == None:
        return None
    action()

def find_contact():
    value = input("Contact details to search --> ")
    show_contact_menu(value)
    
main_menu = [UI.Menuitem("Add new contact", add_contact),
             UI.Menuitem("Delete contact", del_contact),
             UI.Menuitem("Show all contacts", show_contact_menu),
             UI.Menuitem("Find contact", find_contact),
             UI.Menuitem("Exit", on_exit)]

def main():
    db.create_db()
    while True:
        UI.print_menu("______MENU______", main_menu).value()
        
    

if __name__ == "__main__":
    main()

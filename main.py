import db
import UI
import contacts
import validation

# class Flag:
#     def __init__(self, status: bool):
#         self.status = status


def get_val_for_contacts():
    """Возвращает значения для таблицы contacts"""
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
    """Возвращает значения для таблицы numbers"""
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
    print("\nAdding a new contact...")
    contact_rec = get_val_for_contacts()
    if not contact_rec:
        print("Contact not added.") # !!!!!!!!!!!
        return False
    id = contacts.add_contact(contact_rec)
    number_rec = get_val_for_numbers(id)
    if not number_rec:
        print("Contact not added.") # !!!!!!!!!!!
        return False
    contacts.add_number(number_rec)
    print(f"Contact added. Contact ID: {id}")

def exit(flag=True):
    return flag == False

def on_exit():
    db.close_db()


main_menu = [UI.Menuitem("Add new contact", add_contact),
             UI.Menuitem("Exit", on_exit)]

def main():
    db.create_db()
    print_menu_flag = True
    while print_menu_flag:
        UI.print_menu("______MENU______", main_menu).handler()

    
    

if __name__ == "__main__":
    main()
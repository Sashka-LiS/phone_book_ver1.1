import sqlite3 as sq
import valid_funcs as valid


def get_db():
    """Возвращает контакт к БД"""
    connection_db = sq.connect("phone_book.db")
    return connection_db

def get_val_for_contacts(val_tabl_contacts=[]):
    """Возвращает значения для таблицы contacts"""
    surname = input("Фамилия (Для отмены нажми 0)--> ")
    if surname == "0":
        return surname
    val_tabl_contacts.append(surname)
    name = input("Имя (Для отмены нажми 0)--> ")
    if name == "0":
        return name
    while not valid.is_valid_name(name):
        print("Это поля не может быть пустым.")
        name = input("Имя (Для отмены нажми 0)--> ")
        if name == "0":
            return name
    val_tabl_contacts.append(name)
    father_name = input("Отчество (Для отмены нажми 0)--> ")
    if father_name == "0":
        return father_name
    val_tabl_contacts.append(father_name)
    email = input("Email (Для отмены нажми 0)--> ")
    if email == "0":
        return email
    while not valid.is_valid_email(email):
        print("Такой email уже есть в телефонной книге.")
        email = input("Email (Для отмены нажми 0)--> ")
        if email == "0":
            return email
    val_tabl_contacts.append(email)
    return val_tabl_contacts

def get_val_for_numbers(val_tabl_numbers=[]):
    """Возвращает значения для таблицы numbers"""
    number = input("Номер (Для отмены нажми 0)--> ")
    if number == "0":
        return number
    while not valid.is_valid_number(number):
        print("Формат номера должен быть +7... или 8...")
        number = input("Номер (Для отмены нажми 0)--> ")
        if number == "0":
            return number
    val_tabl_numbers.append(number)
    home_number = input("Домашний номер (Для отмены нажми 0)--> ")
    if home_number == "0":
        return home_number
    val_tabl_numbers.append(home_number)
    work_number = input("Рабочий номер (Для отмены нажми 0)--> ")
    if work_number == "0":
        return work_number
    val_tabl_numbers.append(work_number)
    return val_tabl_numbers

def get_response(menu):
    '''Выводит меню и возвращает отклик'''
    print(menu)
    response = input('--> ')
    return response

def get_id_contact():
    """Возвращает ID контакта. Тип ID = integer"""
    id  = int(input("ID контакта (Для отмены нажми 0)--> "))
    return id

def get_new_surname():
    """Возвращает новую фамилия для редактирования контакта"""
    new_surname = input("Новая фамилия контакта (Для отмены нажми 0)--> ")
    return new_surname

def get_new_name():
    """Возвращает новое имя для редактирования контакта"""
    new_name = input("Новое имя для контакта (Для отмены нажми 0)--> ")
    return new_name

def get_new_father_name():
    """Возвращает новое отчество для редактирования контакта"""
    new_father_name = input("Новое отчество контакта (Для отмены нажми 0)--> ")
    return new_father_name

def get_new_email():
    """Возвращает новый email для редактирования контакта"""
    new_email = input("Новый email контакта (Для отмены нажми 0)--> ")
    return new_email

def get_new_number():
    """Возвращает новый номер тел. для редактирования контакта"""
    new_number = input("Новый номер контакта (Для отмены нажми 0)--> ")
    return new_number

def get_new_home_number():
    """Возвращает новый домашний номер для редактирования"""
    new_home_number = input("Новый домашний номер контакта (Для отмены нажми 0)--> ")
    return new_home_number

def get_new_work_number():
    """Возвращает новый рабочий номер для редактирования"""
    new_work_number = input("Новый рабочий номер контакта (Для отмены нажми 0)-->")
    return new_work_number

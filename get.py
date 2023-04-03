import sqlite3 as sq
import validation





def get_val_num(val_tabl_numbers=[]):
    """Возвращает значения для таблицы numbers"""
    number = input("Номер (Для отмены нажми 0)--> ")
    if number == "0":
        return number
    while not validation.is_valid_number(number):
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

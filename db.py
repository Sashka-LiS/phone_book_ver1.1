import sqlite3 as sq


def get_db():
    """Возвращает контакт к БД"""
    connection_db = sq.connect("phone_book.db")
    return connection_db



def create_db():
    """Создание БД"""
    with sq.connect('phone_book.db') as phone_book:
        cursor = phone_book.cursor()

        query = ('''
                CREATE TABLE IF NOT EXISTS contacts
                (
                    id_contact INTEGER PRIMARY KEY,
                    surname TEXT,
                    name TEXT NOT NULL,
                    father_name TEXT,
                    email TEXT
                );

                CREATE TABLE IF NOT EXISTS numbers
                (
                    id_number INTEGER PRIMARY KEY,
                    number TEXT,
                    type TEXT,
                    id_contact INTEGER,
                    FOREIGN KEY (id_contact) REFERENCES contacts (id_contact) ON DELETE CASCADE
                );
                ''')

        cursor.executescript(query)
    return True

def close_db(phone_book=get_db()):
    """Закрывает контакт к БД"""
    phone_book.close()
    return True



# def show_book(phone_book=get_db()):
#     """Возвращает всю БД со всеми контактами"""
#     cursor = phone_book.cursor()
#     all_book = cursor.execute('''SELECT id_contact, surname, name, father_name, email, numbers.number, numbers.home_number, numbers.work_number 
#                       FROM contacts 
#                       JOIN numbers ON contacts.id_contact = numbers.id_number;''').fetchall()
#     cursor.close()
#     return all_book

# def del_contact(id_for_del, phone_book=get_db()):
#     """Удаляет запись из БД по ID"""

#     cursor = phone_book.cursor()    
#     cursor.execute("PRAGMA foreign_keys = on")
#     cursor.execute("DELETE FROM contacts WHERE id_contact = ?", [id_for_del])
#     phone_book.commit()
#     cursor.close()
#     return True

# def search_by_surname(phone_book=get_db()):
#     """Поиск по столбу surname в БД"""
#     surname = input("Фамилия контакта (Для отмены нажми 0)--> ")
#     val_for_search = ["%" + surname + "%"]
#     if surname == "0":
#         return surname
#     cursor = phone_book.cursor()
#     result = cursor.execute("""SELECT id_contact, surname, name, email, numbers.number, numbers.home_number, numbers.work_number
#                                FROM contacts JOIN numbers ON contacts.id_contact = numbers.id_number
#                                WHERE surname LIKE ?;""", val_for_search).fetchall()
#     cursor.close()
#     return result

# def search_by_name(phone_book=get_db()):
#     """Поис по столбу name в БД"""
#     name = input("Имя контакта (Для отмены нажми 0)--> ")
#     val_for_search = ["%" + name + "%"]
#     if name == "0":
#         return name
#     cursor = phone_book.cursor()
#     result = cursor.execute("""SELECT id_contact, surname, name, father_name, email, numbers.number, numbers.home_number, numbers.work_number
#                                FROM contacts JOIN numbers ON contacts.id_contact = numbers.id_number
#                                WHERE name LIKE ?;""", val_for_search).fetchall()
#     cursor.close()
#     return result

# def search_by_father_name(phone_book=get_db()):
#     """Поис по столбу father_name в БД"""
#     father_name = input("Отчество контакта (Для отмены нажми 0)--> ")
#     val_for_search = ["%" + father_name + "%"]
#     if father_name == "0":
#         return father_name
#     cursor = phone_book.cursor()
#     result = cursor.execute("""SELECT id_contact, surname, name, email, numbers.number, numbers.home_number, numbers.work_number
#                                FROM contacts JOIN numbers ON contacts.id_contact = numbers.id_number
#                                WHERE father_name LIKE ?;""", val_for_search).fetchall()
#     cursor.close()
#     return result

# def search_by_email(phone_book=get_db()):
#     """Поис по столбу email в БД"""
#     email = input("Email контакта (Для отмены нажми 0)--> ")
#     val_for_search = ["%" + email + "%"]
#     if email == "0":
#         return email
#     cursor = phone_book.cursor()
#     result = cursor.execute("""SELECT id_contact, surname, name, email, numbers.number, numbers.home_number, numbers.work_number
#                                FROM contacts JOIN numbers ON contacts.id_contact = numbers.id_number
#                                WHERE email LIKE ?;""", val_for_search).fetchall()
#     cursor.close()
#     return result

# def search_by_number(phone_book=get_db()):
#     """Поиск по столбу number в БД"""
#     number = input("Номер контакта (Для отмены нажми 0)--> ")
#     val_for_search = ["%" + number + "%"]
#     if number == "0":
#         return number
#     cursor = phone_book.cursor()
#     result = cursor.execute("""SELECT id_contact, surname, name, email, numbers.number, numbers.home_number, numbers.work_number
#                                FROM contacts JOIN numbers ON contacts.id_contact = numbers.id_number
#                                WHERE number LIKE ?;""", val_for_search).fetchall()
#     cursor.close()
#     return result

# def serach_by_home_number(phone_book=get_db()):
#     """Поиск по столбу home_number в БД"""
#     home_number = input("Домашний номер контакта (Для отмены нажми 0)--> ")
#     val_for_search = ["%" + home_number + "%"]
#     if home_number == "0":
#         return home_number
#     cursor = phone_book.cursor()
#     result = cursor.execute("""SELECT id_contact, surname, name, email, numbers.number, numbers.home_number, numbers.work_number
#                                FROM contacts JOIN numbers ON contacts.id_contact = numbers.id_number
#                                WHERE home_number LIKE ?;""", val_for_search).fetchall()
#     cursor.close()
#     return result

# def search_by_work_number(phone_book=get_db()):
#     """Поиск по стоблу work_number в БД"""
#     work_number = input("Рабочий номер контакта (Для отмены нажми 0)--> ")
#     val_for_search = ["%" + work_number + "%"]
#     if work_number == "0":
#         return work_number
#     cursor = phone_book.cursor()
#     result = cursor.execute("""SELECT id_contact, surname, name, email, numbers.number, numbers.home_number, numbers.work_number
#                                FROM contacts JOIN numbers ON contacts.id_contact = numbers.id_number
#                                WHERE work_number LIKE ?;""", val_for_search).fetchall()
#     cursor.close()
#     return result

# def edit_surname(new_surname, id_for_edit, phone_book=get_db()):
#     """Редактирует поле surname в БД"""
#     values_for_edit = [new_surname, id_for_edit]
#     cursor = phone_book.cursor()
#     cursor.execute("UPDATE contacts SET surname = ? WHERE id_contact = ?;", values_for_edit)
#     phone_book.commit()
#     cursor.close()
#     return True

# def edit_name(new_name, id_for_edit, phone_book=get_db()):
#     """Редактирует поле name в БД"""
#     values_for_edit = [new_name, id_for_edit]
#     cursor = phone_book.cursor()
#     cursor.execute("UPDATE contacts SET name = ? WHERE id_contact = ?;", values_for_edit)
#     phone_book.commit()
#     cursor.close()
#     return True

# def edit_father_name(new_father_name, id_for_edit, phone_book=get_db()):
#     """Редактирует поле father_name в БД"""
#     values_for_edit = [new_father_name, id_for_edit]
#     cursor = phone_book.cursor()
#     cursor.execute("UPDATE contacts SET father_name = ? WHERE id_contact = ?;", values_for_edit)
#     phone_book.commit()
#     cursor.close()
#     return True

# def the_same_email(new_email, id_for_edit, phone_book=get_db()):
#      """Сравнивает старый email с новым у одного контакта для корректного редактирования поля email в БД"""
#      cursor = phone_book.cursor()
#      old_email = cursor.execute('SELECT email FROM contacts WHERE id_contact = ?;', [id_for_edit]).fetchone()
#      cursor.close()
#      return new_email == old_email[0]

# def edit_email(new_email, id_for_edit, phone_book=get_db()):
#     """Редактирует поле email в БД"""
#     values_for_edit = [new_email, id_for_edit]
#     cursor = phone_book.cursor()
#     cursor.execute("UPDATE contacts SET email = ? WHERE id_contact = ?;", values_for_edit)
#     phone_book.commit()
#     cursor.close()
#     return True

# def edit_number(new_number, id_for_edit, phone_book=get_db()):
#     """Редактирует поле number в БД"""
#     values_for_edit = [new_number, id_for_edit]
#     cursor = phone_book.cursor()
#     cursor.execute("UPDATE numbers SET number = ? WHERE id_number = ?;", values_for_edit)
#     phone_book.commit()
#     cursor.close()
#     return True

# def edit_home_number(new_home_number, id_for_edit, phone_book=get_db()):
#     """Редактируе поле home_number в БД"""
#     values_for_edit = [new_home_number, id_for_edit]
#     cursor = phone_book.cursor()
#     cursor.execute("UPDATE numbers SET home_number = ? WHERE id_number = ?;", values_for_edit)
#     phone_book.commit()
#     cursor.close()
#     return True

# def edit_work_number(new_work_number, id_for_edit, phone_book=get_db()):
    """Редактирует поле work_number в БД"""
    values_for_edit = [new_work_number, id_for_edit]
    cursor = phone_book.cursor()
    cursor.execute("UPDATE numbers SET work_number = ? WHERE id_number = ?;", values_for_edit)
    phone_book.commit()
    cursor.close()
    return True
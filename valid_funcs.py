import get_funcs as get


def is_valid_email(email, phone_book=get.get_db()):
    """Проверка email на дубликат в БД"""
    cursor = phone_book.cursor()
    if email == None or email == '':
        return True
    exist_email = cursor.execute("SELECT email FROM contacts WHERE email = ?", [email]).fetchone()
    cursor.close()
    return exist_email is None

def is_valid_name(name):
    """Проверка имени на валидность"""
    if not name:
        return False
    return True

def is_valid_number(number):
    """Проверяет правильность ввода номера"""
    if not number:
        return False
    if number[0:2] != '+7' and number[0] != '8':
        return False
    return True

def is_valid_id(id, list_contacts):
    '''Проверка на вхождение ID в список контактов для манипулиций'''
    list_id = []
    for contact in list_contacts:
        for value in contact:
            if type(value) == int:
                list_id.append(value)
    return id in list_id

import db


def is_valid_email(email, phone_book=db.get_db()):
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



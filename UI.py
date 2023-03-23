

def render_menu(key_menu=None):
    if key_menu == "main_menu":
        strings_for_main_menu = ["\n__________МЕНЮ__________",
                                 "1 - Добавить контакт",
                                 "2 - Показать телефонную книгу",
                                 "3 - Удалить контакт",
                                 "4 - Найти контакт",
                                 "5 - Редактировать контакт",
                                 "0 - Выход"]
        for string in strings_for_main_menu:
            print(string)
        existing_responses = [char for string in strings_for_main_menu for char in string if char.isdigit()]
        response = None
        while response not in existing_responses:
            response = input(" --> ")
        return response

    elif key_menu == "search_menu":
        strings_for_search_menu = ["\n_______МЕНЮ ПОИСКА_______",
                                   "В каком столбе искать контакт?",
                                   "1 - Фамилия",
                                   "2 - Имя",
                                   "3 - Отчество",
                                   "4 - Email",
                                   "5 - Номер",
                                   "6 - Домашний номер",
                                   "7 - Рабочий номер",
                                   "0 - Отмена"]
        for string in strings_for_search_menu:
            print(string)
        existing_responses = [char for string in strings_for_search_menu for char in string if char.isdigit()]
        response = None
        while response not in existing_responses:
            response = input(" --> ")
        return response
    
    elif key_menu == "edit_menu":
        strings_for_edit_menu = ["\n_____МЕНЮ РЕДАКТИРОВАНИЯ_____",
                                 "Какое поле отредактировать?",
                                 "1 - Фамилия",
                                 "2 - Имя",
                                 "3 - Отчество",
                                 "4 - Email",
                                 "5 - Номер",
                                 "6 - Домашний номер",
                                 "7 - Рабочий номер",
                                 "0 - Отмена"]
        for string in strings_for_edit_menu:
            print(string)
        existing_responses = [char for string in strings_for_edit_menu for char in string if char.isdigit()]
        response = None
        while response not in existing_responses:
            response = input(" --> ")
        return response
    



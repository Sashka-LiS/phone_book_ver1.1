main_menu = ["\n__________МЕНЮ__________",
             "1 - Добавить контакт",
             "2 - Показать телефонную книгу",
             "3 - Удалить контакт",
             "4 - Найти контакт",
             "5 - Редактировать контакт",
             "0 - Выход"]

search_menu = ["\n_______МЕНЮ ПОИСКА_______",
               "В каком столбе искать контакт?",
               "1 - Фамилия",
               "2 - Имя",
               "3 - Отчество",
               "4 - Email",
               "5 - Номер",
               "6 - Домашний номер",
               "7 - Рабочий номер",
               "0 - Отмена"]

edit_menu = ["\n_____МЕНЮ РЕДАКТИРОВАНИЯ_____",
             "Какое поле отредактировать?",
             "1 - Фамилия",
             "2 - Имя",
             "3 - Отчество",
             "4 - Email",
             "5 - Номер",
             "6 - Домашний номер",
             "7 - Рабочий номер",
             "0 - Отмена"]


def render_menu(menu):
        for string in menu:
            print(string)
        existing_responses = [char for string in menu for char in string if char.isdigit()]
        response = None
        while response not in existing_responses:
            response = input(" --> ")
        return response





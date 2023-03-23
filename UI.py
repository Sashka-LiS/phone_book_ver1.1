

def render_menu(key_menu=None):
    strings_for_all_menu = [
                        "\n__________МЕНЮ__________", #0
                        "1 - Добавить контакт", #1
                        "2 - Показать телефонную книгу", #2
                        "3 - Удалить контакт", #3
                        "4 - Найти контакт", #4
                        "5 - Редактировать контакт", #5
                        "0 - Выход", #6
                        "\n_______МЕНЮ ПОИСКА_______", #7
                        "В каком столбе искать контакт?", #8
                        "1 - Фамилия", #9
                        "2 - Имя", #10
                        "3 - Отчество", #11
                        "4 - Email", #12
                        "5 - Номер", #13
                        "6 - Домашний номер", #14
                        "7 - Рабочий номер", #15
                        "0 - Отмена", #16
                        "\n_____МЕНЮ РЕДАКТИРОВАНИЯ_____", #17
                        "Какое поле отредактировать?" #18
                        ]
    if key_menu == "main_menu":
        strings_for_main_menu = [strings_for_all_menu[0],
                                 strings_for_all_menu[1],
                                 strings_for_all_menu[2],
                                 strings_for_all_menu[3],
                                 strings_for_all_menu[4],
                                 strings_for_all_menu[5],
                                 strings_for_all_menu[6]]
        for string in strings_for_main_menu:
            print(string)
        existing_responses = [char for string in strings_for_main_menu for char in string if char.isdigit()]
        response = None
        while response not in existing_responses:
            response = input(" --> ")
        return response

    elif key_menu == "search_menu":
        strings_for_search_menu = [strings_for_all_menu[7],
                                   strings_for_all_menu[8],
                                   strings_for_all_menu[9],
                                   strings_for_all_menu[10],
                                   strings_for_all_menu[11],
                                   strings_for_all_menu[12],
                                   strings_for_all_menu[13],
                                   strings_for_all_menu[14],
                                   strings_for_all_menu[15],
                                   strings_for_all_menu[16]]
        for string in strings_for_search_menu:
            print(string)
        existing_responses = [char for string in strings_for_search_menu for char in string if char.isdigit()]
        response = None
        while response not in existing_responses:
            response = input(" --> ")
        return response
    
    elif key_menu == "edit_menu":
        strings_for_edit_menu = [strings_for_all_menu[17],
                                 strings_for_all_menu[18],
                                 strings_for_all_menu[9],
                                 strings_for_all_menu[10],
                                 strings_for_all_menu[11],
                                 strings_for_all_menu[12],
                                 strings_for_all_menu[13],
                                 strings_for_all_menu[14],
                                 strings_for_all_menu[15],
                                 strings_for_all_menu[16],]
        for string in strings_for_edit_menu:
            print(string)
        existing_responses = [char for string in strings_for_edit_menu for char in string if char.isdigit()]
        response = None
        while response not in existing_responses:
            response = input(" --> ")
        return response
    



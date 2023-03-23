import valid_funcs as valid
import db_funcs as db
import get_funcs as get
from pprint import pprint


main_menu = '''\n________МЕНЮ________
1 - Добавить контакт
2 - Показать телефонную книгу
3 - Удалить контакт
4 - Найти контакт
5 - Редактировать контакт
0 - Выход'''

search_menu = '''\nВ каком столбе искать контакт?
1 - Фамилия
2 - Имя
3 - Отчество
4 - Email
5 - Номер
6 - Домашний номер
7 - Рабочий номер
0 - Отмена'''

edit_menu = '''\nКакое поле контакта отредактировать?
1 - Фамилия
2 - Имя
3 - Отчество
4 - Email
5 - Номер
6 - Домашний номер
7 - Рабочий номер
0 - Отмена'''


def main():
    db.create_db()
    show_main_menu = True
    while show_main_menu:
        main_response = get.get_response(main_menu)
        if main_response == "0":
            db.exit()
            show_main_menu = False

        elif main_response == "1":
            val_tabl_contacts = get.get_val_for_contacts()
            if val_tabl_contacts == "0":
                print("\nКонтакт не добавлен.")
                continue
            val_tabl_numbers = get.get_val_for_numbers()
            if val_tabl_numbers == "0":
                print("\nКонтакт не добавлен.")
                continue
            db.add_contact_mode(val_tabl_contacts, val_tabl_numbers)
            print("\nКонтакт добавлен.")
            
        elif main_response == "2":
            print()
            pprint(db.show_book())
            print()

        elif main_response == "3":
            names_for_del = db.search_by_name()
            if names_for_del == "0":
                continue
            if not names_for_del:
                print("\nКонтакт не найден.")
                continue
            else:
                print()
                pprint(names_for_del)
                print()
            id_for_del = get.get_id_contact()
            if id_for_del == 0:
                print("\nКонтакт не удален.")
                continue
            if not valid.is_valid_id(id_for_del, names_for_del):
                print("\nID нет в списке. Контакт не удален.")
                continue
            db.del_contact(id_for_del)
            print("\nКонтакт удален.")

        elif main_response == "4":
            show_search_menu = True
            while show_search_menu:
                search_response = get.get_response(search_menu)
                if search_response == "0":
                    show_search_menu = False

                elif search_response == "1":
                    found_surnames = db.search_by_surname()
                    if found_surnames == "0":
                        continue
                    if not found_surnames:
                        print("\nКонтакт не найден.")
                    else:
                        print()
                        pprint(found_surnames)
                        print()

                elif search_response == "2":
                    found_names = db.search_by_name()
                    if found_names == "0":
                        continue
                    if not found_names:
                        print("\nКонтакт не найден.")
                    else:
                        print()
                        pprint(found_names)
                        print()

                elif search_response == "3":
                    found_father_names = db.search_by_father_name()
                    if found_father_names == "0":
                        continue
                    if not found_father_names:
                        print('\nКонтакт не найден.')
                    else:
                        print()
                        pprint(found_father_names)
                        print()

                elif search_response == "4":
                    found_emails = db.search_by_email()
                    if found_emails == "0":
                        continue
                    if not found_emails:
                        print("\nКонтакт не найден.")
                    else:
                        print()
                        pprint(found_emails)
                        print()

                elif search_response == "5":
                    found_numbers = db.search_by_number()
                    if found_numbers == "0":
                        continue
                    if not found_numbers:
                        print("\nКонтакт не найден.")
                    else:
                        print()
                        pprint(found_numbers)
                        print()
                
                elif search_response == "6":
                    found_home_numbers = db.serach_by_home_number()
                    if found_home_numbers == "0":
                        continue
                    if not found_home_numbers:
                        print("\nКонтакт не найден.")
                    else:
                        print()
                        pprint(found_home_numbers)
                        print()
                
                elif search_response == "7":
                    found_work_numbers = db.search_by_work_number()
                    if found_work_numbers == "0":
                        continue
                    if not found_work_numbers:
                        print("\nКонтакт не найден.")
                    else:
                        print()
                        pprint(found_work_numbers)
                        print()
                
                else:
                    print("\nНет такой команды.")
        
        elif main_response == "5":
            names_for_editing = db.search_by_name()
            if names_for_editing == "0":
                continue
            else:
                print()
                pprint(names_for_editing)
                print()
            id_for_edit = get.get_id_contact()
            if id_for_edit == 0:
                continue
            if not valid.is_valid_id(id_for_edit, names_for_editing):
                print("\nID нет в списке. Контакт не отредактирован.")
                continue
            show_edit_menu = True
            while show_edit_menu:
                edit_response = get.get_response(edit_menu)
                if edit_response == "0":
                    show_edit_menu = False
                
                elif edit_response == "1":
                    new_surname = get.get_new_surname()
                    if new_surname == "0":
                        continue
                    db.edit_surname(new_surname, id_for_edit) 
                    print("\nКонтакт отредактирован.")
                
                elif edit_response == "2":
                    new_name = get.get_new_name()
                    while not valid.is_valid_name(new_name):
                        print("Это поля не может быть пустым.")
                        new_name = get.get_new_name()
                    if new_name == "0":
                        continue
                    db.edit_name(new_name, id_for_edit)
                    print("\nКонтакт отредактирован.")

                elif edit_response == "3":
                    new_father_name = get.get_new_father_name()
                    if new_father_name == "0":
                        continue
                    db.edit_father_name(new_father_name, id_for_edit)
                    print("\nКонтакт отредактирован.")

                elif edit_response == "4":
                    new_email = get.get_new_email()
                    if db.the_same_email(new_email, id_for_edit):
                        print("\nКонтакт отредактирован.")
                        continue
                    while not valid.is_valid_email(new_email):
                        print("Такой email уже есть в телефонной книге.")
                        new_email = get.get_new_email()
                    if new_email == "0":
                        continue
                    db.edit_email(new_email, id_for_edit)
                    print("\nКонтакт отредактирован.")

                elif edit_response == "5":
                    new_number = get.get_new_number()
                    if new_number == "0":
                        continue
                    while not valid.is_valid_number(new_number):
                        print("Формат номера должен быть +7... или 8...")
                        new_number = get.get_new_number()
                        if new_number == "0":
                            break
                    db.edit_number(new_number, id_for_edit)
                    print("\nКонтакт отредактирован.")

                elif edit_response == "6":
                    new_home_number = get.get_new_home_number()
                    if new_home_number == "0":
                        continue
                    db.edit_home_number(new_home_number, id_for_edit)
                    print("\nКонтакт отредактирован.")
                
                elif edit_response == "7":
                    new_work_number = get.get_new_work_number()
                    if new_work_number == "0":
                        continue
                    db.edit_work_number(new_work_number, id_for_edit)
                    print("\nКонтакт отредактирован.")
                
                else:
                    print("\nНет такой команды.")

        else:
            print("\nНет такой команды.")
    print('\nХорошего дня!')

if __name__ == "__main__":
    main()
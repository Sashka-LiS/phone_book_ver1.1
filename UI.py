class Menuitem:
    def __init__(self, title, handler):
        self.title = title
        self.handler = handler


def is_valid_response(response, menu):
    if not response.isdigit() or int(response) <= 0 or int(response) > len(menu):
        return False
    return True


def print_menu(name_menu, menu):
    num_item = 0
    print()
    print(name_menu)
    for item in menu:
        num_item += 1
        print(f"{num_item} - {item.title}")
    response = (input("Select a menu item --> "))
    while not is_valid_response(response, menu):
        response = (input("Select a menu item --> "))
    return menu[int(response)-1]


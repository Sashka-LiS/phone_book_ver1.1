class Menuitem:
    def __init__(self, title, value):
        self.title = title
        self.value = value

def is_valid_response(response, menu):
    if not response.isdigit() or int(response) <= 0 or int(response) > len(menu):
        return False
    return True

def print_menu(name_menu: str, menu: list)-> Menuitem:
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

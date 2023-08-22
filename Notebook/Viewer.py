from Notebook.Manager import Manager


class Viewer:
    def __init__(self, manager: Manager):
        self.__manager = manager

    def show_menu(self):
        if len(self.__manager.notes) >= 1:
            menu_choice = input("[Create] [Save] [Edit] [Read] [Delete] [Exit] -> ")
        else:
            menu_choice = input("[Create] -> ")

        while menu_choice.lower() not in ("create", "save", "edit", "read", "delete", "exit"):
            menu_choice = input("Не знаю такой команды, давай по новой -> ")

        return menu_choice

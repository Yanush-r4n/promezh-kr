from Notebook.Converter import Converter
from Notebook.JSONManager import JSONManager
from Notebook.Manager import Manager
from Notebook.Viewer import Viewer


def save(converter: Converter):
    return converter.save()


def read(converter: Converter, note_id: str):
    return converter.read(note_id)


def valid_id():
    manager.show_notes()
    user_id = input("Введи ID заметки -> ")

    while user_id not in [saved_id for saved_id in manager.notes]:
        user_id = input("Не нахожу такого ID, попытайся её раз -> ")

    return user_id


manager = Manager()
viewer = Viewer(manager)

print("Добро пожаловать в редактор заметок!\n")
flag = False
while not flag:
    menu_choice = viewer.show_menu()

    if menu_choice == "create":
        note = manager.create()

    elif menu_choice == "save":
        save(JSONManager(manager))

    elif menu_choice == "edit":
        edit_choice = valid_id()
        manager.edit(edit_choice)

    elif menu_choice == "read":
        read_choice = valid_id()
        read(JSONManager(manager), read_choice)

    elif menu_choice == "delete":
        read_choice = valid_id()
        manager.delete(read_choice)

    elif menu_choice == "exit":
        flag = True
        print("До свидания!")

import datetime
from Notebook.Note import Note


class Manager:
    def __init__(self):
        self.__notes = {}

    def create(self):
        note = Note()
        note.title = input("Введите заголовок вашей заметки:\n")
        note.body = input("Введите текст вашей заметки:\n")
        note.last_update = datetime.date.today().strftime("%d.%m.%y")
        self.__notes[note.id] = note
        print("Заметка создана!\n")

    def edit(self, note_id: str):
        self.__notes[note_id].title = input("Введите новый заголовок вашей заметки:\n")
        self.__notes[note_id].body = input("Введите новый текст вашей заметки:\n")
        self.__notes[note_id].last_update = datetime.date.today().strftime("%d.%m.%y")
        print("Заметка изменена!\n")

    def delete(self, note_id: str):
        del self.__notes[note_id]
        print("Заметка удалена!\n")

    def show_notes(self):
        for note_id, note in self.__notes.items():
            print(f"[{note_id}] {note.title}")

    @property
    def notes(self):
        return self.__notes

import json
from Notebook.Converter import Converter


class JSONManager(Converter):
    def save(self):
        dict_memory = {}
        for note in self._manager.notes.values():
            note_dict = {"Title": note.title,
                         "ID": note.id,
                         "Date": note.date,
                         "Last update": note.last_update,
                         "Body": note.body}
            dict_memory[note.id] = note_dict

        with open("D:\\Projects\\GB\\Notebook\\Memory.json", "w") as file:
            json.dump(dict_memory, file, indent=4)

    def read(self, note_id: str):
        self.save()

        with open("D:\\Projects\\GB\\Notebook\\Memory.json", "r") as file:
            data = json.load(file)

        if note_id in data:
            selected_note = data[note_id]
            print(f"""[{selected_note['ID']}] Дата создания: {selected_note['Date']}""")
            print(f"""последнее изменение: {selected_note['Last update']}""")
            print(f"""{selected_note['Title']}""")
            print(f"""{selected_note['Body']}""")
        else:
            print("Нет заметки с таким ID")

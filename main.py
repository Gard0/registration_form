from tkinter import *
import json

window = Tk()

text1 = Entry()
text1.pack()

text2 = Entry()
text2.pack()


def save(login, password):
    file = open("data_reg.json", "r")
    array_data_reg = json.load(file)
    file.close()
    array_data_reg.append({"login": login, "password": password})
    file = open("data_reg.json", "w")
    json.dump(array_data_reg, file)
    file.close()


def click():
    save(text1.get(), text2.get())


button = Button()
button["text"] = "Conform"
button["command"] = click
button.pack()

window.mainloop()

from class1 import Verification
from tkinter import Tk, Button


class My_app(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry('400x400')
        self.setUI()

    def setUI(self):
        Button(self, text='OK').pack()


root = My_app()
root.mainloop()

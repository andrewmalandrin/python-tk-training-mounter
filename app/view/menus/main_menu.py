from tkinter import Frame

class MainMenu(Frame):
    '''Main menu class'''
    def __init__(self, parent):
        self.parent = parent
        super().__init__(self.parent)

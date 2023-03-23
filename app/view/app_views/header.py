from tkinter import Frame, Label

class AppHeader(Frame):
    '''Application Header Class'''
    def __init__(self, parent, title):
        super().__init__(parent)
        self.title = title
        self.grid(row=0, column=0, sticky='W'+'E'+'N'+'S')
        self.config(bg='#112')
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        title_label = Label(self, text=title, bg='#112', fg='#88F', font=('Arial Black', 25))
        title_label.grid(row=0, column=0, sticky='wens')

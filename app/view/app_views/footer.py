from tkinter import Frame, Button

class AppFooter(Frame):
    '''Application Header Class'''
    def __init__(self, parent):
        super().__init__(parent)
        self.grid(row=2, column=0, sticky='W'+'E'+'N'+'S')
        self.config(bg='#112')
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # close_button = button
        # # close_button = Button(self, text='Fechar', command=close_fn, bg='#223', fg='#88F', borderwidth=0)
        # close_button.grid(row=0, column=0)

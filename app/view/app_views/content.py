from tkinter import Button, Frame, Scrollbar, Listbox
from app.helpers.enums.app_content_buttons import AppContentButtonsEnum
from app.view.app_views.content_views.content_data_frame import ContentDataFrame

class AppContent(Frame):
    '''Application Content Class'''
    def __init__(self, parent):
        super().__init__(parent)
        self.grid(row=1, column=0, sticky='W'+'E'+'N'+'S')
        self.config(bg='#445')
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=5)
        self.grid_columnconfigure(0, weight=1)

        content_buttons_frame = Frame(self, bg='#334')
        content_buttons_frame.grid_rowconfigure(0, weight=1)
        content_buttons_frame.grid_columnconfigure(0, weight=0)
        content_buttons_frame.grid_columnconfigure(1, weight=0)
        content_buttons_frame.grid_columnconfigure(2, weight=0)
        content_buttons_frame.grid(row=0, column=0, sticky='NSWE')

        data_frame = ContentDataFrame(self)
        add_button = Button(
            content_buttons_frame,
            text=AppContentButtonsEnum.ADD_EXERCISE,
            command=data_frame.create_new_row,
            bg='#223',
            fg='#88F',
            borderwidth=0
            )
        add_button.grid(row=0, column=0, ipadx=3, ipady=3, padx=(10, 0), pady=10 ,sticky='NE')
        add_button.bind("<Enter>", lambda e: add_button.config(bg='#445', fg='#99F'))
        add_button.bind("<Leave>", lambda e: add_button.config(bg='#223', fg='#88F'))
        
        open_button = Button(
            content_buttons_frame,
            text=AppContentButtonsEnum.OPEN_FILE,
            command=data_frame.open_file,
            bg='#223',
            fg='#88F',
            borderwidth=0
            )
        open_button.grid(row=0, column=1, ipadx=3, ipady=3, padx=(10, 0), pady=10 ,sticky='NE')
        open_button.bind("<Enter>", lambda e: open_button.config(bg='#445', fg='#99F'))
        open_button.bind("<Leave>", lambda e: open_button.config(bg='#223', fg='#88F'))

        save_button = Button(
            content_buttons_frame,
            text=AppContentButtonsEnum.SAVE_TRAINING,
            command=data_frame.save_data_frame_to_xlsx,
            bg='#223',
            fg='#88F',
            borderwidth=0
            )
        save_button.grid(row=0, column=2, ipadx=3, ipady=3, padx=(10, 0), pady=10 ,sticky='NE')
        save_button.bind("<Enter>", lambda e: save_button.config(bg='#445', fg='#99F'))
        save_button.bind("<Leave>", lambda e: save_button.config(bg='#223', fg='#88F'))

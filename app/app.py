# import tkinter as tk
import pandas as pd
from app.helpers.enums.training_columns import TrainingColumnsEnum

from app.view.app_views.header import AppHeader
from app.view.app_views.content import AppContent
from app.view.app_views.footer import AppFooter

from tkinter import Button, Tk, Frame, PhotoImage


class TkinterApp(Tk):
    '''Class da aplicação'''
    
    
    def __init__(self):
        super().__init__()
        
        _title = "Training Mounter"

        # App Settings
        self.title(_title)
        self.geometry('1024x768')
        self.resizable(False, False)
        self.iconphoto(False, PhotoImage(file="app/assets/title_icon.png"))
        self.config()
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # App Container
        container = Frame(self, bg='#223')
        container.grid(row=0, column=0, sticky='W'+'E'+'N'+'S')
        # container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_rowconfigure(1, weight=5)
        container.grid_rowconfigure(2, weight=1)
        container.grid_columnconfigure(0, weight=1)

        header = AppHeader(container, _title)
        
        content = AppContent(container)
        
        footer = AppFooter(container)
        close_button = Button(footer, text='Fechar', command=self.quit, bg='#223', fg='#88F', borderwidth=0)
        close_button.grid(row=0, column=0)
        close_button.bind("<Enter>", lambda e: close_button.config(bg='#445', fg='#99F'))
        close_button.bind("<Leave>", lambda e: close_button.config(bg='#223', fg='#88F'))

# def add_blank_cell(parent_frame: tk.Frame):
    



# def get_data_from_spreadsheet():
#     pass

# def show_frame():
#     pass

# def start():
#     window = tk.Tk()
#     window.title('Diet Maker 1.0')
#     window.geometry('800x600')
#     window.config(
#         bg='#223'
#     )
#     window.grid_rowconfigure(0, weight=1)
#     window.grid_columnconfigure(0, weight=1)

#     # region Container Frame
#     container = tk.Frame(window)
#     container.grid(row=0, column=0, sticky='W'+'E'+'N'+'S')
#     container.grid_rowconfigure(0, weight=1)
#     container.grid_columnconfigure(0, weight=1)
#     # container.grid_propagate(0)
#     # endregion Container Frame

#     main_menu_options = ['Zerar treino', 'Salvar treino', 'Adicionar Exercício']
    
#     # region Main Menu Frame
#     main_menu_width = 800
#     main_menu_frame = tk.Frame(container, width=main_menu_width, height=600, bg='#223')
#     main_menu_frame.grid(row=0, column=0, padx=10, pady=5, sticky='W'+'E'+'N'+'S')
#     main_menu_frame.grid_columnconfigure(0, weight=1)
#     main_menu_frame.grid_rowconfigure(0, weight=1)
#     main_menu_frame.grid_rowconfigure(1, weight=4)
#     main_menu_frame.grid_rowconfigure(2, weight=1)
#     # main_menu_frame.grid_propagate(0)
#     # endregion Main Menu Frame

#     # region Main Menu Title
#     main_menu_title = tk.Label(main_menu_frame, text='Menu Principal', bg='#112', fg='#88F', width=main_menu_width)
#     main_menu_title.grid(row=0, column=0, sticky='W'+'E'+'N'+'S')
#     main_menu_title.grid_rowconfigure(0, weight=1)
#     main_menu_title.grid_columnconfigure(0, weight=1)
#     # endregion Main Menu Title

#     # region Main Menu Content Frame
#     main_menu_content_frame = tk.Frame(main_menu_frame, bg='#334', width=main_menu_width)
#     main_menu_content_frame.grid(row=1, column=0, sticky='W'+'E'+'N'+'S')
#     main_menu_content_frame.grid_rowconfigure(0, weight=1)
#     main_menu_content_frame.grid_rowconfigure(1, weight=4)
#     main_menu_content_frame.grid_columnconfigure(0, weight=1)


#     # main_menu_content_frame.grid_columnconfigure(1, weight=1)
#     # main_menu_content_frame.grid_propagate(0)
#     # endregion Main Menu Content Frame
    
#     # region Content Data Frame
#     data_frame = tk.Frame(main_menu_content_frame, bg='#445')
#     data_frame.grid(row=1, columnspan=len(main_menu_options), sticky='W'+'E'+'N'+'S')
#     data_frame.grid_rowconfigure(0, weight=1)
#     training_columns = list(TrainingColumnsEnum)
#     actual_df = pd.DataFrame(columns=training_columns)
#     print(actual_df)
    
#     # endregion Content Data Frame
    
#     # region Content Buttons
#     buttons: list = [tk.Button(main_menu_content_frame, text=option, bg='#112', fg='#88F', borderwidth=0) for option in main_menu_options]
#     main_menu_content_frame.grid_rowconfigure(0, weight=1)
#     for index in range(0, len(buttons)):
#         main_menu_content_frame.grid_columnconfigure(index, weight=1)
#     for index, button in enumerate(buttons):
#         if button == 'Adicionar Exercícico':
#             button.grid(row=0, column=index, pady=5, padx=5, sticky='W'+'E'+'N'+'S', command= lambda: add_blank_line(len(list(TrainingColumnsEnum)), data_frame))
#         else:
#             button.grid(row=0, column=index, pady=5, padx=5, sticky='W'+'E'+'N'+'S')

#     # endregion Content Buttons


#     # region Data Table Entries
    
#     for idx, df_column in enumerate(actual_df.columns):
#         data_frame.grid_columnconfigure(idx, weight=1)
#         data_label = tk.Label(data_frame, text=df_column, borderwidth=1, relief='solid', bg='#445', fg='#AAF')
#         data_label.grid(row=0, column=idx, ipadx=3, ipady=3, sticky='W'+'E'+'N')

#     if len(actual_df.index) > 0:
#         data_set = []
#         for x in range(1, len(actual_df.conlumns)):
#             for y in range(0, len(actual_df.index)+1):
#                 data_entry = tk.Entry(data_frame, textvariable=data_set[x])
#                 data_entry.grid(row=x, column=y, sticky='W'+'E'+'N')

#     # endregion Data Table Entries
    
#     button = tk.Button(main_menu_frame, text='Fechar', command=window.quit, bg='#112', fg='#88F', borderwidth=0)
#     # button.grid(row=1, column=0, padx=5, pady=5)
#     button.grid(row=2, column=0)
#     #button.grid_propagate(0)
#     button.update()
#     print(button.winfo_height())
    

#     window.mainloop()
    
#     return 'Fim'
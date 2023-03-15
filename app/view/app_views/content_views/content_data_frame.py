from app.helpers.enums.training_columns import TrainingColumnsEnum
from datetime import datetime
from pandas import DataFrame
from tkinter import Frame, Label, Entry, Scrollbar, Canvas, Toplevel

import pandas as pd

class ContentDataFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.grid(row=1, column=0, sticky='W'+'E'+'N'+'S')
        self.config(bg='#446')
        # self.grid_rowconfigure(0, weight=1)
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_columnconfigure(1, weight=1)
        # self.grid_propagate(False)

        self.rows: list = []
        columns = [i.value for i in list(TrainingColumnsEnum)]
        self.data_df: DataFrame = DataFrame(columns=columns)
        


        # scrollbar.grid_columnconfigure(0, weight=0)
        # scrollbar.grid_rowconfigure(0, weight=0)

        self.canvas = Canvas(self, bd=0, bg='#447')
        self.canvas.pack(side='left', fill='both', expand=True)
        # self.canvas.grid(row=0, column=0, sticky='wnes')
        # self.canvas.grid_rowconfigure(0, weight=0)
        # self.canvas.grid_columnconfigure(0, weight=0)

        self.scrollbar = Scrollbar(self, orient='vertical', bg='#449')
        # self.scrollbar.grid(row=0, column=len(list(TrainingColumnsEnum)), sticky='ns')
        # self.scrollbar.grid(row=0, column=1, sticky='ns')
        self.scrollbar.pack(side='right', fill='y')
        self.scrollbar.config(command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set, width=768)

        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion= self.canvas.bbox('all')))

        self.table_frame = Frame(self.canvas, bg='#FFF')
        # self.canvas.grid_propagate(False)

        canvas_window = self.canvas.create_window((0,0), window=self.table_frame, anchor='nw')

        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

        for idx, df_column in enumerate(self.data_df.columns):
            self.table_frame.grid_columnconfigure(idx, weight=1)
            data_label = Label(self.table_frame, text=df_column, borderwidth=1, relief='solid', bg='#445', fg='#AAF')
            data_label.grid(row=0, column=idx, ipadx=3, ipady=3, sticky='W'+'E'+'N')
        self.canvas.update_idletasks()
        self.canvas.configure(scrollregion= self.canvas.bbox('all'))
        
        self.create_first_row()
        self.canvas.itemconfig(canvas_window, width=self.canvas.winfo_width()-4)

    def create_first_row(self):
        self.new_row_dict: dict = {}
        # self.table_frame.grid_rowconfigure(1, weight=1)
        for idx, df_column in enumerate(self.data_df.columns):
            self.new_row_dict[df_column] = Entry(self.table_frame, borderwidth=1, relief='solid')
            self.new_row_dict[df_column].grid(row=1, column=idx, ipadx=3, ipady=3, sticky='wen')
        self.canvas.update_idletasks()
        self.canvas.configure(scrollregion= self.canvas.bbox('all'))
        self.rows.append(self.new_row_dict)
    
    def create_new_row(self):
        self.new_row_dict: dict = {}
        rows_number = len(self.rows)
        rows = [*self.rows]
        rows.reverse()
        # self.table_frame.grid_rowconfigure(rows_number+1, weight=1)
        for idx_row, row in enumerate(rows):
            for idx, cell in enumerate(row.values()):
                cell.grid(row=idx_row+2, column=idx, ipadx=3, ipady=3, sticky='W'+'E'+'N')
        for idx, df_column in enumerate(self.data_df.columns):
            self.new_row_dict[df_column] = Entry(self.table_frame, borderwidth=1, relief='solid')
            self.new_row_dict[df_column].grid(row=1, column=idx, ipadx=3, ipady=3, sticky='wen')
        self.rows.append(self.new_row_dict)
        self.canvas.update_idletasks()
        self.canvas.configure(scrollregion= self.canvas.bbox('all'))
        #self.scrollbar.grid(rowspan=len(self.rows)+1, column=len(list(TrainingColumnsEnum)), sticky='ns')
    
    def create_new_row2(self):
        self.new_row_dict: dict = {}
        rows_number = len(self.rows)
        # self.table_frame.grid_rowconfigure(rows_number+1, weight=1)
        for idx, df_column in enumerate(self.data_df.columns):
            self.new_row_dict[df_column] = Entry(self.table_frame, borderwidth=1, relief='solid')
            self.new_row_dict[df_column].grid(row=2+len(self.rows), column=idx, ipadx=3, ipady=3, sticky='wen')
        self.rows.append(self.new_row_dict)
        self.canvas.update_idletasks()
        self.canvas.configure(scrollregion= self.canvas.bbox('all'))
        #self.scrollbar.grid(rowspan=len(self.rows)+1, column=len(list(TrainingColumnsEnum)), sticky='ns')
    
    def new_row_popup(self):
        popup = Toplevel(self)
        #popup.geometry("800x600")
        popup.title('Adicionar exercício')
        content_frame = Frame(popup)
        content_frame.pack()
        Label(content_frame, text="Informe os dados sobre o exercício.").pack(padx=10, pady=10)
    
    def saved_successfully_message_popup(self):
        popup = Toplevel(self)
        #popup.geometry("800x600")
        popup.title('Planilha criada com sucesso')
        content_frame = Frame(popup)
        content_frame.pack()
        Label(content_frame, text="Planilha gerada com sucesso na pasta trainings").pack(padx=10, pady=10)
        
    
    def save_data_frame_to_xlsx(self):
        new_rows_list = []
        datetime_now = datetime.now()
        datetime_format = '%d%m%Y--%H-%M'
        datetime_str = datetime_now.strftime(datetime_format)

        for row in self.rows:
            new_dict: dict = {}
            for key, value in row.items():
                new_dict[key] = [value.get()]
            new_rows_list.append(pd.DataFrame(new_dict))
        
        rows_df = pd.concat(new_rows_list)
        writer = pd.ExcelWriter(f"trainings/Training_sheet-{datetime_str}.xlsx", engine="xlsxwriter")
        rows_df.to_excel(writer, 'Training', index=False)
        writer.close()
        self.saved_successfully_message_popup()

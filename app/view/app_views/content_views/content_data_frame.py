from app.helpers.enums.training_columns import TrainingColumnsEnum
from datetime import datetime
from pandas import DataFrame
from tkinter import Frame, Label, Entry, Scrollbar, Canvas, Toplevel, filedialog

import pandas as pd

class ContentDataFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.grid(row=1, column=0, sticky='W'+'E'+'N'+'S')
        self.config(bg='#446')

        self.rows: list = []
        columns = [i.value for i in list(TrainingColumnsEnum)]
        self.data_df: DataFrame = DataFrame(columns=columns)

        self.canvas = Canvas(self, bd=0, bg='#447')
        self.canvas.pack(side='left', fill='both', expand=True)
        self.canvas.bind_all('<MouseWheel>', self.mouse_wheel)

        self.scrollbar = Scrollbar(self, orient='vertical', bg='#449')
        self.scrollbar.pack(side='right', fill='y')
        self.scrollbar.config(command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set, width=768)

        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion= self.canvas.bbox('all')))

        self.table_frame = Frame(self.canvas, bg='#FFF')

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
        for idx, df_column in enumerate(self.data_df.columns):
            self.new_row_dict[df_column] = Entry(self.table_frame, borderwidth=1, relief='solid', bg='#667', fg='#BBF')
            self.new_row_dict[df_column].grid(row=1, column=idx, ipadx=5, ipady=3, sticky='wen')
        self.canvas.update_idletasks()
        self.canvas.configure(scrollregion= self.canvas.bbox('all'))
        self.rows.append(self.new_row_dict)
    
    def create_new_row(self):
        self.new_row_dict: dict = {}
        rows = [*self.rows]
        rows.reverse()
        for idx_row, row in enumerate(rows):
            for idx, cell in enumerate(row.values()):
                cell.grid(row=idx_row+2, column=idx, ipadx=3, ipady=3, sticky='W'+'E'+'N')
        for idx, df_column in enumerate(self.data_df.columns):
            self.new_row_dict[df_column] = Entry(self.table_frame, borderwidth=1, relief='solid', bg='#667', fg='#BBF')
            self.new_row_dict[df_column].grid(row=1, column=idx, ipadx=3, ipady=3, sticky='wen')
        self.rows.append(self.new_row_dict)
        self.canvas.update_idletasks()
        self.canvas.configure(scrollregion= self.canvas.bbox('all'))

    def new_row_popup(self):
        popup = Toplevel(self)
        popup.title('Adicionar exercício')
        content_frame = Frame(popup)
        content_frame.pack()
        Label(content_frame, text="Informe os dados sobre o exercício.").pack(padx=10, pady=10)
    
    def saved_successfully_message_popup(self, file_path: str = 'training'):
        popup = Toplevel(self)
        popup.title('Planilha criada com sucesso')
        content_frame = Frame(popup)
        content_frame.pack()
        Label(content_frame, text=f"Planilha gerada com sucesso no caminho: {file_path}").pack(padx=10, pady=10)
        
    
    def save_data_frame_to_xlsx(self):

        # TODO: Adjust Columns Size and implement save as and open file features
        pd.set_option('max_colwidth', None)
        new_rows_list = []
        datetime_now = datetime.now()
        datetime_format = '%d%m%Y--%H-%M'
        datetime_str = datetime_now.strftime(datetime_format)

        file_path = filedialog.asksaveasfilename(
            initialdir="D:/documentos",
            filetypes=[('Xlsx file','.xlsx')],
            defaultextension=[('.xlsx', '*.xlsx')]
        )

        for row in self.rows:
            new_dict: dict = {}
            for key, value in row.items():
                new_dict[key] = [value.get()]
            new_rows_list.append(pd.DataFrame(new_dict))
        
        sheets_list = []
        for row in new_rows_list:
            if (row['Treino'][0] not in sheets_list):
                sheets_list.append(row['Treino'][0])
        
        writer = pd.ExcelWriter(file_path, engine="xlsxwriter")
        for sheet in sheets_list:
            sheet_df = []
            for df_row in new_rows_list:
                if df_row['Treino'][0] == sheet:
                    sheet_df.append(df_row.drop('Treino', axis=1))
            rows_df = pd.concat(sheet_df)
            rows_df.to_excel(writer, f"Treino_{sheet}", index=False)
            self.adjust_sheet_columns_width(f"Treino_{sheet}", writer, rows_df)

        writer.close()
        
        self.saved_successfully_message_popup(file_path=file_path)

    def adjust_sheet_columns_width(self, sheet_name: str, excel_writer: pd.ExcelWriter, data_frame: pd.DataFrame):

        worksheet = excel_writer.sheets[sheet_name]
        for idx, column in enumerate(data_frame):
            series = data_frame[column]
            max_len = max(
                (
                    series.astype(str).map(len).max(),
                    len(str(series.name))
                )
            ) + 1
            worksheet.set_column(idx, idx, max_len)

    def open_file(self):
        file_path = filedialog.askopenfilename(
            initialdir="D:/documentos",
            filetypes=[('Xlsx file','.xlsx')],
            defaultextension=[('.xlsx', '*.xlsx')]
        )
        for row in self.rows:
            print(row)
            for key, _value in row.items():
                row[key].grid_forget()
        
        self.rows = []
        rows_count = 0
        file = pd.ExcelFile(file_path)
        for sheet_idx, sheet in enumerate(file.sheet_names):
            sheet_df = pd.read_excel(file_path, sheet)
            sheet_df.reset_index()
            for row_idx, row in sheet_df.iterrows():
                new_row: dict = {TrainingColumnsEnum.training: Entry(self.table_frame, borderwidth=1, relief='solid', bg='#667', fg='#BBF')}
                new_row[TrainingColumnsEnum.training].grid(row=rows_count + 1, column=0, ipadx=3, ipady=3, sticky='wen')
                new_row[TrainingColumnsEnum.training].insert(0, sheet.replace('Treino_', ''))
                for column_idx, column in enumerate(sheet_df.columns):
                    new_row[column] = Entry(self.table_frame, borderwidth=1, relief='solid', bg='#667', fg='#BBF')
                    new_row[column].grid(row=rows_count + 1, column=column_idx + 1, ipadx=3, ipady=3, sticky='wen')
                    new_row[column].insert(0, row[column])
                rows_count += 1
                self.rows.append(new_row)
                self.canvas.update_idletasks()
                self.canvas.configure(scrollregion= self.canvas.bbox('all'))
                print(self.rows)

    def mouse_wheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), 'units')

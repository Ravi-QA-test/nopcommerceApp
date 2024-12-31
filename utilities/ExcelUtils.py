import openpyxl

def get_row_count(file,sheet_name):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheet_name]
    return (sheet.max_row)

def get_column_count(file,sheet_name):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheet_name]
    return (sheet.max_column)

def read_data(file,sheet_name,rownum,columnno):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheet_name]
    return sheet.cell(row=rownum, column=columnno).value

def write_data(file,sheet_name,rownum,columnno,data):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheet_name]
    sheet.cell(row=rownum, column=columnno).value = data
    workbook.save(file)


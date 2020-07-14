import openpyxl

wb = openpyxl.load_workbook('exemplo.xlsx')
planilha = wb.active
for linha in planilha.rows:
    print(linha)

import openpyxl

wb = openpyxl.load_workbook('exemplo.xlsx')

planilha = wb['Plan1']
print(planilha)

# print(planilha['A1':'C5'])

for linha in planilha['A1':'C5']:
    for coluna in linha:
        print('{} --> {}'.format(coluna.coordinate, coluna.value))
import openpyxl

wb = openpyxl.load_workbook('exemplo.xlsx')

planilhas = wb.sheetnames
print(planilhas)

planilha = wb['Plan1']
print(planilha)

planilha.title = 'Mouse'

wb.save('exemplo2.xlsx')
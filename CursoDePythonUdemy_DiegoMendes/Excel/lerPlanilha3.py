import openpyxl

wb = openpyxl.load_workbook('exemplo.xlsx')
planilha = wb.active

# linha = planilha[1]
# for celula in linha:
#     print(celula.value)


for coluna in planilha.iter_cols(min_row=1, min_col=2, max_col=3, max_row=5):
    for celula in coluna:
        print(celula.value)
    print('')
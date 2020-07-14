import docx
doc = docx.Document('exemplo.docx')

textoLista = []
for linha in doc.paragraphs:
    textoLista.append(linha.text)

print(textoLista)


texto = '\n'.join(textoLista)
print('\n{}'.format(texto))
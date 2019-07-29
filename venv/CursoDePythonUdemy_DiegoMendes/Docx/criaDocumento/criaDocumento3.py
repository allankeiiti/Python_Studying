import docx
from docx.shared import Pt

doc = docx.Document()

doc.add_paragraph('Curso de Python')

linha = doc.add_paragraph('Nesse curso de ')
linha.add_run('Python')
linha.add_run(' trabalhamos com ')
linha.add_run('SQLite')
linha.add_run(' e com o ')
linha.add_run('Word')

linha.runs[1].underline = True
linha.runs[3].bold = True
linha.runs[4].italic = True
linha.runs[5].font.size = Pt(24)
linha.runs[0].font.size = Pt(14)
#alterando a fonte
linha.runs[0].font.name = 'Arial'
linha.runs[2].font.name = 'Courier'

doc.save('Doc2.docx')

print(len(linha.runs))


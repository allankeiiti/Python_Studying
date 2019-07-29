import docx
doc = docx.Document('exemplo.docx')

print(doc.paragraphs[0].text)
print(doc.paragraphs[0].style)

doc.paragraphs[0].style = 'List Bullet'
doc.save('novo.docx')

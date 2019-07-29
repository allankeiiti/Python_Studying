import docx
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = docx.Document()

doc.add_paragraph('Logotipo do python')
doc.paragraphs[0].align = WD_ALIGN_PARAGRAPH.CENTER
doc.paragraphs[0].runs[0].font.size = Pt(24)

doc.add_picture('logo.png', width=docx.shared.Cm(12), height=docx.shared.Cm(12))
doc.paragraphs[1].align = WD_ALIGN_PARAGRAPH.CENTER

doc.save('documento_imagem.docx')
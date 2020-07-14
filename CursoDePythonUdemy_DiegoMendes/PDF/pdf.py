from fpdf import FPDF

#P - Portrait
#L - Landscape

#
pdf = FPDF('P','mm', 'A4')

pdf.add_page()

#Antes de inserir um texto no pdf, devemos determinar a fonte a ser usada
#1º argumento é a fonte, 2º argumento é o estilo (Bold, italic, sublimed) 3º argumento é o tamanho da fonte
pdf.set_font('Arial','B', 16)

#colocando célula de 60mm (6cm) da esquerda para direita, 20mm de altura e o texto a ser inserido.
# 1 - terá borda, 0 - não terá borda
# 0 - direita, 1 - esquerda, 2 - Abaixo
# L - LEFT, R - RIGHT
pdf.cell(60, 20, 'Curso de Python com FPDF', 0, 1, 'L')
pdf.cell(60, 20, 'Curso de Python com FPDF', 1, 1, 'C')
pdf.cell(60, 20, 'Curso de Python com FPDF', 0, 1, 'R')

pdf.output('exemplo.pdf','F')
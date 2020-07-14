from fpdf import FPDF

pdf = FPDF('P','mm','A4')

pdf.add_page()

pdf.set_font('Arial','',16)

# o parametro "In" é 1 se vai ter quebra de linha e 0 se não vai ter quebra de linha

pdf.cell(60, 10,'Texto 1', 1, 0, 'R', 0)
pdf.cell(60, 20,'Texto 2', 1, 0, 'L', 0)
pdf.cell(60, 20,'Texto 3', 1, 0, 'L', 0)
pdf.add_page()
pdf.set_font('Arial','',16)
pdf.cell(0, 5,'Texto 1', 1, 1, 'L')
pdf.set_font('Times','I',12)
pdf.cell(0, 5,'Texto 2', 1, 1, 'C')
pdf.set_font('Times','B',11)
pdf.cell(0, 5,'Texto 3', 1, 1, 'R')

pdf.output('Texto.pdf','F')
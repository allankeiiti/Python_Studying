from fpdf import FPDF

pdf = FPDF('P','mm','A4')
pdf.add_page()

pdf.image('logo.png', 70,80)
pdf.image('logo.png', 70,160,20,20)
pdf.image('https://cdn4.iconfinder.com/data/icons/scripting-and-programming-languages/512/Python_logo-512.png',70,200,20,20)
pdf.add_page()

pdf.set_font('Arial','B',15)

convidados = [['Allan Keiiti Nakakita','(11)983234535',2,'A'],
             ['Rennan Siqueira','(13)123312313',1,'B'],
             ['Bruna Mendes','(21)928388382',4,'C'],
             ['Regina Márcia','(14)983246666',3,'B'],
             ['Diego Rodrigues','(11)987223421',5,'A']]

pdf.cell(0,20,'Convidados Jantar Beneficente',1,1,'C',0)
pdf.set_font('courier','B',12)
subtitulo = '{:<35}      {:<20}      {:<3}       Setor'.format('Nome','Telefone','Qtd','Depto')
pdf.cell(0,20,subtitulo,0,1)

pdf.set_font('courier','',12)
for convidado in convidados:
    nome = convidado[0]
    telefone = convidado[1]
    pessoas = convidado[2]
    depto = convidado[3]
    pdf.cell(0,10,'{:<35}      {:<20}      {:<3}       Setor'.format(nome, telefone, pessoas, depto),0,1,'C',0)

pdf.output('imagem.pdf','F')
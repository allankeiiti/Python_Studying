'''
PDF - Listas e Cores no arquivo PDF
Curso de Python

Diego M. Rodrigues
'''

from fpdf import FPDF

pdf = FPDF('P', 'mm', 'A4')

pdf.add_page()

# Lista com os convidados do Jantar Beneficente
convidados = [['Ana Braga',       '(11) 9.9262-9312', 2, 'A'],
              ['Bruna Mendes',    '(19) 9.7862-1344', 1, 'B'],
              ['Regina Márcia',   '(21) 9.8872-3942', 4, 'C'],
              ['Sergio Garcia',   '(14) 9.8292-8313', 3, 'B'],
              ['Diego Rodrigues', '(11) 9.8722-3421', 5, 'A']]

# Subtítulo
pdf.set_font('Arial', 'B', 16)

pdf.set_draw_color(255, 111, 105)   # Cor: Vermelho um pouco claro
pdf.set_fill_color(255, 111, 105)
pdf.set_text_color(255, 255, 255)   # Cor: Branco
pdf.cell(0, 20, 'Convidados Jantar Beneficente', 1, 1, 'C',
                                                            1) # Força o preenchimento

pdf.set_draw_color(255, 204, 92)
pdf.set_fill_color(255, 204, 92)
pdf.set_text_color(0, 0, 0)         # Cor: Preto
subtitulo = '{:<35}    {:<20}    {:<3}   Setor'.format('Nome', 'Telefone', 'Qtd')
pdf.set_font('courier', 'B', 12)
pdf.cell(0, 20, subtitulo, 0, 1)

# Adicionando os convidados que estão ba Lista no arquivo PDF
pdf.set_font('courier', '', 12)

i=0
for convidado in convidados:
    nome = convidado[0]
    telefone = convidado[1]
    pessoas = convidado[2]
    setor = convidado[3]

    if i == 1:
        pdf.set_text_color(200, 0, 0)   # Cor: Vermelho
        i = 0
    else:
        pdf.set_text_color(50, 50, 50)  # Cor: Cinza
        i = 1

    pdf.cell(0, 10, '{:<35}    {:<20}     {:1}      {:1}'.format(nome,
                                                              telefone,
                                                              pessoas,
                                                              setor), 0, 1)

# Escrevendo o arquivo PDF no disco
pdf.output('convidados_cores.pdf', 'F')
import sqlite3

con = sqlite3.connect('cadastro.db')

cursor = con.cursor()

lista = [('Allan3','Rua Z','38119011848','allan3@fmu.br','29322931'),
         ('Allan4', 'Rua ZX', '38119011848', 'allan4@fmu.br', '29322931'),
         ('Allan5', 'Rua ZXA', '38119011848', 'allan5@fmu.br', '29322931'),
         ('Allan6', 'Rua ZXA1', '38119011848', 'allan6@fmu.br', '29322931')]

cursor.executemany("""
    INSERT INTO cadastros (nome, endereco, cpf, email, cel) VALUES (?,?,?,?,?)
""", lista)
print('Lista inserida com sucesso')
con.commit()
con.close()
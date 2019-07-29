import sqlite3

con = sqlite3.connect('cadastro.db')

cursor = con.cursor()

cursor.execute("""
INSERT INTO cadastros (nome, endereco, cpf, email, cel) 
VALUES ('Allan2','Rua Y','38119011848','allan2@fmu.br','29322931');
""")

print('Inserido Regisro!')
con.commit()
con.close()
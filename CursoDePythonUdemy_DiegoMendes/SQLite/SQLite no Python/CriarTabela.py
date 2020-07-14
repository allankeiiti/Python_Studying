import sqlite3

con = sqlite3.connect('cadastro.db')

cursor = con.cursor()

cursor.execute("""
CREATE TABLE cadastros (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    endereco TEXT NOT NULL,
    cpf VARCHAR(11) NOT NULL,
    email TEXT NOT NULL,
    cel VARCHAR(17) NOT NULL
);
""")

print('tabela gerada com sucesso!')
con.close()
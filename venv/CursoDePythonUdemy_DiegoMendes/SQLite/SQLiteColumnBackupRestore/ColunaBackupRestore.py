import sqlite3
import io
con = sqlite3.connect('bancoCRUD.db')
cursor = con.cursor()

# cursor.execute('''
#     ALTER TABLE usuarios
#     ADD COLUMN email TEXT
# ''')
nome_tabela = 'usuarios'

#PEGANDO COLUNAS DA TABELA
cursor.execute('PRAGMA table_info({})'.format(nome_tabela))
colunas = [tupla[1] for tupla in cursor.fetchall()]
print(colunas)

# for coluna in colunas:
#     print(coluna)

# LISTANDO TABELAS DO DB
cursor.execute('''
    SELECT name FROM sqlite_master WHERE type='table' ORDER BY name
''')
print('Tabelas: ')
for tabela in cursor.fetchall():
    print(tabela)

# FAZENDO BACKUP DO DB
with io.open('usuarios_dump.sql', 'w') as f:
    for linha in con.iterdump():
        f.write('%s\n' % linha)
print('Backup realizado com sucesso')

# FAZENDO RESTORE DO DB
f = io.open('usuarios_dump.sql','r')
sql = f.read()
cursor.execute(sql)

con.commit()
con.close()
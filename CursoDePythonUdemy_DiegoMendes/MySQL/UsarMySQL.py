import mysql.connector

'''
MySQL - Usando o MySQL no Python
'''

conn = mysql.connector.connect(user='root',
                               password='root',
                               host='127.0.0.1',
                               database='cadastros')

cursor = conn.cursor()
cursor.execute("SELECT * FROM usuarios")
for linha in cursor.fetchall():
    print('ID....: {}'.format(linha[0]))
    print('NOME..: {}'.format(linha[2]))

conn.close()

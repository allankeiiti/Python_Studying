from sqlite3 import connect
from __init__ import check_txt
from os import remove, path

# Implantando SQLite3 no jogo da forca, substituindo o uso do arquivo .txt

remove('palavras.db') if path.exists('palavras.db') else none
conn = connect('palavras.db')
c = conn.cursor()

def create_table():
  c.execute('CREATE TABLE IF NOT EXISTS palavras('
            'ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,'
            'PALAVRA TEXT)')
  conn.commit()

def insert_values_var(word):
  c.execute("INSERT INTO palavras (PALAVRA) VALUES (?)",(word,))
  conn.commit()

def select_all():
  c.execute('SELECT * FROM palavras')
  for tuples in c.fetchall():
    print(tuples)

create_table()
c.execute("INSERT INTO palavras VALUES(001, 'scrum')")

# Isto é para "brincar"

palavras = check_txt('list')
for palavra in palavras:
  insert_values_var(palavra)

insert_values_var('blader')

select_all()

c.close()
conn.close()

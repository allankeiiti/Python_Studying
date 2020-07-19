"""
Script responsável por criar o arquivo .db do SQLite e responsável por popular a tabela.

Digite as palavras que deseja inserir no Banco embarcaco no arquivo palavras.txt do mesmo diretório
"""

from sqlite3 import connect
# from DataScienceAcademy_Scripts.Cap5.start import check_txt
# from os import remove, path
from random import randint

# Implantando SQLite3 no jogo da forca, substituindo o uso do arquivo .txt

# remove('palavras.db') if path.exists('palavras.db') else none
conn = connect('palavras.db')
c = conn.cursor()


def create_table():
  """
    Cria a tabela no Banco.
  :return: None
  """
  c.execute('CREATE TABLE IF NOT EXISTS palavras('
            'ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,'
            'PALAVRA TEXT)')
  conn.commit()


def insert_values_var(word):
  """
  :param word: Palavra a ser inserida no Banco.
  :return: None
  """
  c.execute("INSERT INTO palavras (PALAVRA) VALUES (?)",(word,))
  conn.commit()

def select_all():
  """
    Imprime todas as palavras presentes no Banco.
  :return: None
  """
  c.execute('SELECT * FROM palavras')
  for tuples in c.fetchall():
    print(tuples)

def random_word():
  """
  Source: https://stackoverflow.com/questions/2854011/get-a-list-of-field-values-from-pythons-sqlite3-not-tuples-representing-rows/23115247
  :return: Palavra a ser sorteada para o jogo da Forca.
  """
  conn = connect('palavras.db')
  c = conn.cursor()
  conn.row_factory = lambda cursor, row: row[0]
  tuples = c.execute('SELECT PALAVRA FROM palavras').fetchall()
  palavras = []
  for tupl in tuples:
    t = str(tupl).replace("('", "").replace(",)", "").replace("'", "")
    palavras.append(t)
  c.close()
  conn.close()
  return palavras[randint(0, len(palavras) - 1)]


create_table()

# # Lendo o arquivo txt e populando a tabela.
# palavras = check_txt('list')
# for palavra in palavras:
#  insert_values_var(palavra)

# select_all()

c.close()
conn.close()

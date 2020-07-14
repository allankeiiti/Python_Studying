# Biblioteca que requisita uma página de um web site
import urllib.request

url_to_scrap = 'https://www.python.org'

# Definindo a conexão com a URL
with urllib.request.urlopen(url_to_scrap) as url:
    page = url.read()

# Imprime o conteúdo
print(page)

# Extrai apenas os textos da página HTML que é raspada
from bs4 import BeautifulSoup

soup = BeautifulSoup(page, "html.parser")

soup.title

soup.title.string

soup.a

soup.find_all("a")

tables = soup.find('table')

print(tables)
'''
Exercícios de fixação - Tratamento de Erros
Curso de Python

Diego M. Rodrigues

Exercício 1
---
Crie uma calculadora onde o usuário final irá entrar com 2 números 
inteiros, depois iremos exibir um menu com as seguintes opções:
• Somar
• Subtrair
• Multiplicar
• Dividir
• Raiz quadrada
• Digitar outros números
• Sair
Ele irá selecionar a opção desejada e o script Python irá realizar 
a operação matemática. Então o resultado será exibido na tela. 
Depois de visualizar o resultado, o usuário retorna para o menu.
O teste se o número digitado é um inteiro deve ser realizado como 
apresentado nas aulas anteriores.
Você deve também tratar os erros na divisão e no cálculo das 
raízes quadradas.
'''
def showMenu():
    print("1 - Somar\n2 - Subtrainr\n3 - Multiplicar\n4 - Dividir\n5 - Raiz Quadrada(sqrt)\n6 - Digitar Outros Números\n0 - Sair")

try:
    num1 = int(input('TYPE NUM1: '))
    num2 = int(input('TYPE NUM2: '))
    opt = int(input('TYPE OPTION: '))
    while opt != 0:
        showMenu()
        opt = int(input('TYPE OPTION: '))
except ValueError:
    print('VALUE ERROR')

'''
Exercício 2
---
Crie um arquivo de texto com nomes de restaurantes.
Realize a leitura desse arquivo utilizando o with e apresente os 
resultados na tela.
'''


x,y = 4,6
a = "{x}".format(x = y), + 2,"{y}".format(y = 10)
print(a)

a = [1,5,7]
b = [2,5,6]
c = a.extend(b)
print(c)
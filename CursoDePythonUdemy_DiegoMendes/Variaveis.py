# Curso ed Python
#método que realiza leitura de argumentos inteiros
nome = str(input('Digite o seu nome: '))

print('Bem-vindo {}'.format(nome))

num1 = int(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))

def methodSum(x,y):
    sum = x + y
    print('{} + {} = {}'.format(x, y, sum))
    print(type(sum))

methodSum(num1, num2)

#classes isnumeric() verifica se o valor pode ser convertido para numérico
#isalpha() verifica se o valor é uma letra
#isalnum() alfanumérico
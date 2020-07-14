'''
Exercicio 1
Crie um Script onde o usuário digita 2 números e vc exibe a soma deles

Exercicio 2
Receba do usuario uma inf. do teclado, eixba o tipo primitivo dessa informação recebida e depois
todas as possíveis informações sobre ela.
'''
'''
print("Exercicio 1\nCrie um Script onde o usuário digita 2 números e vc exibe a soma deles")
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
print(num1+num2)

'''

print('Exercicio 2\nReceba do usuario uma inf. do teclado, eixba o tipo primitivo dessa informação recebida e depois\ntodas as possíveis informações sobre ela.')
var = input('Digite um valor para var: ')
    print('O tipo do var é: ',type(var))
    print('É numérico?: ', var.isnumeric())
    print('É letra?: ', var.isalpha())
    print('É alfanumérico?: ',var.isalnum())
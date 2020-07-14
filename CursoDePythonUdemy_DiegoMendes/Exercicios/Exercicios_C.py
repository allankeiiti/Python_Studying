'''
Wz: 1
Crie um script onde o usuário digita um numero inteiro, então você exibe na tela seu sucessor e antecessor.

num = int(input('Digite um número: '))
print('Número: {}.\nAntecessor: {}.\nSucessor: {}.'.format(num, num-1, num+1))

Ex: 2
Leia um número e exiba na tela o seu dobro, triplo e sua raiz quadrada

num = int(input('Digite um número: '))
print('Número: {}.\nDobro: {}.\nTriplo: {}.\nRaiz Quadrada: {:.0f}.'.format(num, num*2, num*3, num**(1/2)))

Ex: 3
Faça um script que leia as duas notas de um aluno, depois mostre sua média. lembre de utilizar o print com format.além
de prestar atenção na ordem da precedencia dos operadores.

nota1 = int(input('Digite a nota 1 do aluno: '))
nota2 = int(input('Digite a nota 2 do aluno: '))
media = (nota1+nota2)/2
print('nota 1: {}.\nnota 2: {}.\nmédia: {:.0f}.'.format(nota1,nota2,media))

Ex: 4
Leia um valor em metros, depois exiba esse valor em centimetros e milimetros

metros = float(input('Digite um comprimento em metros, o mesmo será convertido em km, cm e mm! \nDigite o valor: '))
print('me: {:.2f}.\nkm: {:.2f}.\ncm: {:.2f}.\nmm: {:.2f}'.format(metros, metros*0.001, metros*100, metros*1000))

Ex: 5
O user digita um inteiro e você exibe a tabuada dele

num = int(input('Digite um inteiro, será exibida a tabuada dele!\nDigite o valor: '))
for i in range(10):
    print('{} x {} = {}'.format(num, i+1, num * (i+1)))

Ex: 6
Solicite que a pessoa digite quanto ela tem de dinheiro na carteira. Depois exiba quantos dólares ela possui, usando a conversão
US$ 1,00 = R$ 3,30 (var / 3.30)

option = input('D - Converter US$ para R$. \nR - Converter R$ para US$.\nDigite a opção: ')
if option == 'R' or option == 'r':
    valor = float(input('Digite um valor em R$ a ser convertido para US$: '))
    print('R$: {:.2f}.\nUS$: {:.2f}.'.format(valor, valor * 3.3))
elif option == 'D' or option == 'd':
    valor = float(input('Digite um valor em US$ a ser convertido para R$: '))
    print('R$: {:.2f}.\nUS$: {:.2f}.'.format(valor / 3.3, valor))
else:
    print('Opção inválida! Script encerrado')

Ex: 7
Leia a altura e largua de uma parede. Exiba a área da parede e quantidade de tinta necessária para pintá-la. Considerando
que 1Litro de tinta pinta uma área de 3 metros quadrados.

height = float(input('Digite a altura da parede: '))
width = float(input('Digite a largura da parede: '))
area = height * width
print('Altura: {:.2f}\nLargura: {:.2f}\nMetos Quadrados: {:.2f}'.format(height,width,area))
print('Será Necessário {:.2f} de Tinta para pintar esta parede!'.format(area/3))

Ex. 8
No script o usuário digita o valor de um produto. depois você mostra um novo valor com 10% de desconto.

productName = input('Digite o nome do produto: ')
productCost = float(input('Digite o valor do produto {}: '.format(productName)))

print('O valor com 10% de desconto será de: {:.2f}'.format(productCost*0.9))
'''
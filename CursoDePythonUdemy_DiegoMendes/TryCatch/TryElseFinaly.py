import math

# num = input('Digite um número: ')
# if num.isnumeric():
#     num = float(num)

while True:
    try:
        num = float(input('Digite um número: '))
        break
    except Exception:
        print('Não foi Digitado um número. Tente novamente')

try:
    raiz = math.sqrt(num)
except ValueError as Args:
    print('Não posso calcular a raiz quadrada de números negativos')
    print('Erro: {}'.format(Args))
# except Exception as Args:
#     print('Não posso calcular a raiz quadrada')
#     print('Erro: {}'.format(Args))
else:
    print('A raiz de {:.2f} é {:.2f}'.format(num, raiz))
finally:
    print('Finally')

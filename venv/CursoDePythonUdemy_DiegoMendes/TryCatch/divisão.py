def divisão(x, y):
    try:
        resultado = x / y
    except ValueError:
        print('Erro de valor')
    except ZeroDivisionError:
        print('Erro ao realizar divisão com zero "{}"'.format(0))
    else:
        print('{} / {} = {:.2f}'.format(x, y, resultado))

print(divisão(6,3))
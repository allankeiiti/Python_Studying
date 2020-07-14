'''
Cores no terminal do Python utilizando padrão ANSI
'''

#quando utilizar cores, deve ser utilizado a estrutura abaixo
#\033[m

#\033[ESTILO;COR_TEXTO;COR_FUNDOm

print('\033[0;34;46mTeste de ccr\33[m')
n = 10
print('\033[1;30;47mO número escolhido foi {}\033[m'.format(n))
print('O número escolhido foi {}{}{}'.format('\033[1;30;47m',n,'\033[m'))

idade = int(input('Digite a idade: '))

if idade < 18:
    print('Não entra no bar')
else:
    if idade == 21:
        print('\033[4;30;1mRefri.\033[m')
    elif idade == 60:
        print('\033[4;30;43mCerveja Vodka\033[m')
    else:
        print('\033[1;30;44mÁgua\033[m')

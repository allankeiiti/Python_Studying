import numpy as np
from os import system
import matplotlib.pyplot as plt
# Estatística

A = np.array([15, 23, 63, 94, 75])

# A função numpy mean calcula a média de um array
print('Média',np.mean(A))

# O desvio padrão mostra o quanto de variação ou 'disperção' existe em
# relação à média (ou valor esperado).
# Um baixo desvio padrão indica que os dados tendem a estar próximos da média.
# Um desvio padrão alto indica que os dados estão espalhados por uma gama de valores.
print('Desvio padrão',np.std(A))

# Variância de uma variável aleatória é uma medida da sua dispersão
# estatística, indicando 'o quão longe' em geral os seus valores se
# encontram do valor esperado
print('Variância',np.var(A))

d = np.arange(1, 10)
print(d)
x = np.sum(d)
print(x)

# Retorna o produto dos elementos
print('Produtos',np.prod(d))

# Soma acumulada dos elementos
print('Soma acumulada',np.cumsum(d))

a = np.random.randn(400,2)
print(a)
system('pause')
m = a.mean(0)
print(m, m.shape)

# A bola vermelha é a média
plt.plot(a[:,0], a[:,1], 'o', markersize = 5, alpha = 0.50)
plt.plot(m[0], m[1], 'ro', markersize = 10)
plt.show()

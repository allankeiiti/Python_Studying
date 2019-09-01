import numpy as np
import matplotlib.pyplot as plt

# Outras operações com Arrays - NUMPY

# Slicing
a = np.diag(np.arange(3))
print('{} diag ->\n {}'.format(np.arange(3), a))
print('a[1,1]:',a[1,1],'a[1]:',a[1])
b = np.arange(10)
print('b:',b,'b[2:9:3]:',b[2:9:3])

# Comaparação
a = np.array([1, 2, 3, 4])
b = np.array([4, 2, 2, 4])
print('A == B:\n',a == b)

print(np.array_equal(a, b))
print('a.min():',a.min(),'a.max():',a.max())
print('b.min():',b.min(),'b.max():',b.max())

# Somando um elemento ao Array
print('np.array([1, 2, 3]) + 1.5: ',np.array([1, 2, 3]) + 1.5)

# Usando o método around - a função arredonda os valores "quebrados"
a = np.array([1.2, 1.5, 1.6, 2.5, 3.5, 4.5])
b = np.around(a)
print('a = np.array([1.2, 1.5, 1.6, 2.5, 3.5, 4.5]) -> b = np.around(a): ',b)

# Copiando um array
B = np.array([1, 2, 3, 4])
C = B.flatten()
print('C: ',C)

# Adicionando uma dimensão ao Array
V = np.array([1, 2, 3])
print(V[:, np.newaxis],'\n',V[:, np.newaxis].shape,'\n',V[np.newaxis,:].shape)

# Repetindo os elementos de um Array
print('np.repeat(V, 3): ',np.repeat(V, 3))

# Repetindo os elementos de um array
print('np.tile(V, 3): ',np.tile(V, 3))

# Concatenando
W = np.array([5, 6])
print('np.concatenate((V, W), axis = 0): ',np.concatenate((V, W), axis = 0))

# Copiando arrays
R = np.copy(V)
print(R)
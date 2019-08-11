import numpy as np
from os import path
import matplotlib.pyplot as plt

# Operações com Datasets

filename = path.join('iris.csv')

# Carregando um dataset para dentro de um array
arquivo = np.loadtxt(filename, delimiter=',', usecols = (0,1,2,3), skiprows=1)
print(arquivo)

print(type(arquivo))

# Gerando um plot a partir de um arquivo usando NumPy
var1, var2 = np.loadtxt(filename, delimiter=',', usecols=(0,1), skiprows=1, unpack=True)
plt.show(plt.plot(var1, var2, 'o', markersize=10, alpha=0.75))
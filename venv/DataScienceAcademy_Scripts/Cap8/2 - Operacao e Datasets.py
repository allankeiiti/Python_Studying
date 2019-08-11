import numpy as np
import matplotlib.pyplot as plt

# Operações com DataSets (Fazendo aqui pois estou com problemas no matplotlib no Jupyter

print(np.random.rand(10))
plt.show((plt.hist(np.random.rand(1000))))

print(np.random.randn(5, 5))

plt.show(plt.hist(np.random.randn(1000)))

imagem = np.random.rand(30, 30)
plt.imshow(imagem, cmap = plt.cm.hot)
plt.colorbar()
plt.savefig("out.png")
plt.show()
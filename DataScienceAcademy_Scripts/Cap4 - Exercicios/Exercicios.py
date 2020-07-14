# Exercicio 1 - Crie uma list de 3 elementos e calcule a terceira potência de cada elemento **3
a, b, c = 3, 10, 20
lista = [a**3, b**3, c**3]

# Exercício 2 - Reescreva o código abaixo, usando a função map(). O resultado final deve ser o mesmo!
palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil'.split()
resultado = [[w.upper(), w.lower(), len(w)] for w in palavras]
for i in resultado:
    print(i)

resultadoMap = map(lambda x: [w.upper(), w.lower(), len(w)], palavras)

# Exercício 3 - Calcule a matriz transposta da matriz abaixo.
# Caso não saiba o que é matriz transposta, visite este link: https://pt.wikipedia.org/wiki/Matriz_transposta
# Matriz transposta é um conceito fundamental na construção de redes neurais artificiais, base de sistemas de IA.
matrix = [[1, 2],[3,4],[5,6],[7,8]]
import numpy as np
matrixT = np.array(matrix).T
matrixT = matrixT.tolist()

# Exercício 4 - Crie duas funções, uma para elevar um número ao quadrado e outra para elevar ao cubo.
# Aplique as duas funções aos elementos da lista abaixo.
# Obs: as duas funções devem ser aplicadas simultaneamente.
lista = [0, 1, 2, 3, 4]
def eleva_ao_quadrado(numero):
    return numero ** 2
def eleva_ao_cubo(numero):
    return numero ** 3

listaResultado = [eleva_ao_cubo(eleva_ao_quadrado(numero)) for numero in lista]
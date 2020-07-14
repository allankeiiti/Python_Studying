#agenda = {'Allan':983234535,'João':911245678,'Julia':9872625273}

#amigo = str(input('Buscar: '))

#if amigo in agenda:
#    print('Telefone de {}: {}'.format(amigo ,
#                                      agenda[amigo]))
#else:
#    print('Não tenho o telefone do {}.'.format(amigo))

#POP
#amigo = agenda.pop('Allan')
#print(agenda)
#print(amigo)

#POP ITEM (No pop só retorna o valor, no popitem retorna a chave E o valor
#amigo = agenda.popitem()
#print(amigo)

#agendax = {'Allan':983234535,'João':911245678,'Julia':9872625273}
#agenday = {'Kyo':983234535,'Kaue':911245678,'Julio':9872625273}

#agendax.update(agenday)
#print(agendax)

#for chave, valor in agendax.items():
#    print('{} => {}.'.format(chave, valor))

#chaves = list(agendax.keys())
#valores = list(agendax.values())

#print(chaves)
#print(valores)

chaves =  ['Ana','Bruna','Julia','Regina']
valores = [100,  200,     300,        400]

dicfinal = dict(zip(chaves, valores))
print(dicfinal)
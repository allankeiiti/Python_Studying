import sqlite3

# Criando banco de dados
con = sqlite3.connect('bancoCRUD.db')
cursor = con.cursor()

# Criando Tabela
tableQuery = 'CREATE TABLE usuarios (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,' \
         'nome TEXT NOT NULL,' \
         'endereco TEXT NOT NULL,' \
         'cpf VARCHAR(11) NOT NULL,' \
         'uf VARCHAR(2) NOT NULL)'
# cursor.execute(tableQuery)

option = int(input('Digite uma opcao\n 1 - Insert\n2 - Consultar\n3 - Alterar\n4 - Deletar\n '))
if option == 1:
    # INSERINDO VALORES NO DB
    p_nome = input('Digite o nome a ser inserido no Banco: ')
    p_endereco = input('Digite o nome da rua: ')
    p_cpf = int(input('Digite o CPF de {}: '.format(p_nome)))
    p_uf = input('Digite a UF (Apenas 2 digitos): ')

    cursor.execute('''
    INSERT INTO usuarios (nome, endereco, cpf, uf) VALUES (?,?,?,?)
    ''', (p_nome, p_endereco, p_cpf, p_uf))
elif option == 2:
    # EXIBINDO VALORES DO DB
    cursor.execute('''
        SELECT * FROM usuarios
    ''')

    for linha in cursor.fetchall():
        # print(linha)
        print('Nome.......: {}'.format(linha[0]))
        print('Nome.......: {}'.format(linha[1]))
        print('Endereço...: {}'.format(linha[2]))
        print('CPF........: {}'.format(linha[3]))
        print('UF.........> {}\n'.format(linha[4]))
elif option == 3:
    # ALTERAÇÃO
    id_usuario = int(input('Digite um ID a ser alterado: '))
    novo_nome = input('Digite um novo nome: ')
    cursor.execute('''
    UPDATE usuarios 
    SET nome = ?
    WHERE id = ? 
    ''',(novo_nome, id_usuario))
elif option == 4:
    id_usuario = int(input('Digite um ID a ser removido: '))
    cursor.execute('''
    DELETE FROM usuarios
    WHERE id = ?
    ''', (id_usuario,))
else:
    print('Bye!')

con.commit()
#Fechando a conexão
con.close()
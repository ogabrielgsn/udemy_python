# Métodos úteis dos dicionários em Python 
# get - obtém uma chave 
# pop - Apaga um item com as chave especificada (del)
# popitem - Apaga o últimp item adicinado
# update - Atualiza um dicionário com outro

p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Mirada',
}

#Utilizando o GET
    # print(p1('nome')) # Se a chave não existir traz um erro
    # print(p1.get('nome')) # Caso a chave não exista, irá aparecer NONE na tela 

#Utilizando do Pop
    # nome = p1.pop('nome') #Elimina a chave, mas retorna o valor da chave apagada
    # print(nome)
    # print(p1)

#Utilização do PopItem
    # ultima_chave = p1.popitem() #Remove a ultima chave do dicionário
    # print(ultima_chave)
    # print(p1)

#Formas de utilizar o update, podemos atualizar o dicionário ou trazer uma nova chave
    # p1.update({
    #     'nome': 'novo valor',
    #     'idade': 30,
    # })

#Segunda maneira de usar o update
    #p1.update(nome='novo valor', idade=20)
    #print(p1)

#Terceira maneira de usar o upate - Usando Tupla ou Lista so passar os - [] - 
    # tupla = ('nome', 'novo valor'),
    # p1.update(tupla)
    # print(p1)
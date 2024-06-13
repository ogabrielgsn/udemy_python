# Manipulando chaves e valores em dicionários
pessoa = {}

##
##
chave = 'nome' #Criar chave

pessoa[chave] = 'Luiz Miranda'
pessoa['sobrenome'] = 'Santos' #Outra maneira de cirar uma chave

print(pessoa[chave])#Acessar uma chave

pessoa[chave] = 'Gabriel' #Editar uma chave

del pessoa['sobrenome'] #Apagar a chave (sobrenome)
print(pessoa)


# print(pessoa.get('sobrenome'))
if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])


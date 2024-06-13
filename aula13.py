# Métodos úteis dos dicionários em Python 
# len - quantas chaves 
# keys - iteráveis com as chaves 
# values - iteráveis com os valores
# items - iteráveis com chaves e valores
# setdefault - adicona valor se a chave não existe 
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 20,
}
print(pessoa, type(pessoa))

#Formas de usar o Len 
 # print(pessoa.__len__())
 # print(len(pessoa))

# Formas de usar o Keys
    # print(pessoa.keys()) 
    # print(tuple(pessoa.keys())) #Fazendo a coersao
    # print(list(pessoa.keys())) #Fazendo a coersao

    # for chave in pessoa.keys(): 
    #     print(chave)

    # for chave in pessoa: - Irá retornar a msm coisa se nao tivesse o keys
    #     print(chave)

#Formas de usar o Values
    # print(pessoa.values())
    # print(list(pessoa.values())) #Fazendo a coersao

    # for valor in pessoa.values():
    #     print(valor)

# Formas de usar o Items
    # print(list(pessoa.items())) #Mostra os valores e chaves

    # for chave, valor in pessoa.items():
    #     print(chave, valor)

#Formas de usar o Setdefault  -Traz o valor caso a chave não existir
    # pessoa.setdefault('idade', None)
    # pessoa.setdefault('idade', 0)
    # print(pessoa['idade'])

    # pessoa.setdefault('idade', 30)
    # print(pessoa['idade'])
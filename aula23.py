# List comprehension em Python 
# List comprehension é uma forma rápida para criar listas a partir de iteráveis.

import pprint # Importação de um print - com ele conseguimos manipular a forma que imprimimos 

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

lista = []
for numero in range(10):
    lista.append(numero)

lista = [numero * 2 for numero in range(10)]
# print(lista)

# print(list(range(10)))
# print(lista)
"""
Mapeamento - VEM NA ESQUERDA DO FOR 

Filtro - VEM NA DIREITA DO FOR
"""
#Mapeamento de dados em list comprehension - Fazemos outra lista com modificações, mas mantendo o msm tamanho 
produtos = [
    {'nome': 'p1', 'preco': 20,},
    {'nome': 'p2', 'preco': 10,}, 
    {'nome': 'p3', 'preco': 30,},
]
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} #A gente desempacota e depois fazendo a mudança
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

# print(novos_produtos)
# print(*novos_produtos, sep='\n')
# p(novos_produtos)

#FILTRO - Fazemos modificações na lista, mudando o tamanho dela, precisa ser na frente do For
# lista = [n for n in range(10) if n <= 5]
# print(lista)

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} 
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if produto['preco'] > 10
]
p(novos_produtos)

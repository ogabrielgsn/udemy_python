# Dicionários em Python (tipo direct)
# Dicionários são estruturas de dados do tipo
#par de "chave" e "valor".
#Chaves podem ser consideradas como "índice"
#que vimos na lisra e podem ser de tipos imutáveis 
#como: str, int, float, bool, tuple, etc.
#O valor pode ser de qualquer tipo, incluindo outro dicionário.
#Usamos as chaves - {} - ou classe dict para criar dicionários.
# Imutáveis: str, int, float, bool, tuple
#Mutável: dict, list

#---Outra forma de fazer um dicionário---
#---pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')---

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'numero': 123},
        {'rua': 'outra rua', 'numero': 321},
    ],
}
# print(pessoa, type(pessoa))
print(pessoa['nome']) 
print(pessoa['sobrenome']) 
print(pessoa['idade']) 

print()

for chave in pessoa:
    print(chave, pessoa[chave])
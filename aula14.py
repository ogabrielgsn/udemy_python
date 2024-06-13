# Métodos úteis dos dicionários em Python 
    # Copy - retorna uma cópia rasa (shallow  copy)


#Copy - só copia valores Imutáveis - Logo Listas não são copiadas só redirecionadas
    # d1 = {
    #     'c1': 1,
    #     'c2': 2,
    #     'l1': [0, 1, 2],
    # }

    # d2 = d1.copy()
    # d2['c1'] = 1000
    # d2['l1'][1] = 999999 # Foi redirecionada e não copiada, por conta de ser uma lista
    # print(d1)
    # print(d2)

    #--Redirecionamento--
        # d2 = d1 
        # d2['c1'] = 1000 # Não está copiando - Está so redirecionando
        # print(d1)

#Copia profunda - A onde você pode copiar dados Imutáveis - Copy.deepcopy
import copy

d1 = {
        'c1': 1,
        'c2': 2,
        'l1': [0, 1, 2],
    }

d2 = copy.deepcopy(d1)

d2['c1'] = 1000
d2['l1'][1] = 999999 

print(d1)
print(d2)
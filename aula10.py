#Exercícios
#Crie funções que duplicam, triplicam e quadruplicam 
# O número recebdii como parâmetro

# def duplicar(numero):
#     return numero * 2

# def triplicar(numero):
#     return numero * 3

# def quadruplicar(numero):
#     return numero * 4
    
# print(duplicar(2))
# print(triplicar(2))
# print(quadruplicar(2))


#Complexo
def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)
print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))

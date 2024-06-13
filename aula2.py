"""
Argumentos nomeados e não nomeados em funções Python 
Argumentos nomeado tem nome com sinal de igual
Argumentos não nomeado recebe apenas o argumento (valor)
"""
def soma(x, y, z): #PARAMETROS
    #Definição
    print(f'{x=} {y=} {z=}', '|', 'x + y + z = ', x + y + z) 
                  
soma(1,2,3) #ARGUMETOS
soma(y=2, x=1, z=3)
soma(1, 2, z=5)

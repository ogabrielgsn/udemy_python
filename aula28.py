# dir, hasattr e getattr em Python
#dir - nomes definidos da string
#hasattr - checar o objeto tem um atributo
#getattr - executa o atributo
string = 'Gabriel'
metodo = 'upper'

if hasattr(string, metodo):
    print('Executa upper')
    print(getattr(string, metodo)())
else: 
    print('Não existe o método', metodo)
    

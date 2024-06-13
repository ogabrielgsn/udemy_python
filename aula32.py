# Try, except, else e finally
# a = 18
# b = 0
# c = a / b

try:
    a = 18
    b = 0 # Zero Division Error
    # print(b[0]) # Type Error
    print('Linha 1'[1000]) #Index Error
    c = a / b
    print('Linha 2')
except ZeroDivisionError:
    print('Dividiu por zero')
except NameError:
    print('nome B não está definido')
except (TypeError, IndexError) as error: #as error, objeto do erro 
    print('TypeError + IndexError')
    print('MSG:', error)
    print('Nome:', error.__class__.__name__)
except Exception: #O main da excessão
    print('Erro Desconhecido')

print('CONTINUAR')
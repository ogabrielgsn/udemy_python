# try, except, else e finally
try: 
    print('Abrir arquivo')
    8/0
except ZeroDivisionError: # except para Tratar o erro
    print('Dividiu zero')
else:
    print('NÃO DEU ERRO')
finally: #Sempre será executa, msm que ocorra um erro - Mostra o erro tbm. Não trata a excessão
    print('Fechar arquivo')
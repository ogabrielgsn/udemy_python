import sys # getsizeof ver o tamanho da lista em bits

# Generator expression, Iterables e Iterators em Python 
# Gennerator são funções que sabem pausar em determinada ocasião
# Iterator, trabalha com iteravel é uma classe que necessita do método iter e o método next
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # tem __iter__ e __next__

lista = [n for n in range(1000)]
generator = (n for n in range(1000)) 

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))
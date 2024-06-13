# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
# s1 = set()  # vazio
# s1 = {'Luiz', 1, 2, 3}  # com dados
# print(s1)

# Sets são eficientes para remover valores duplicados de iteráveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# l1 = [1, 2, 3, 3, 3, 3, 3, 3, 3, 1]
# s1 = set(l1) #Convertendo lista para Set
# l2 = list(s1) 
# print(l2)

#Interação
# s1 = {1,2,3}
# print(3 in s1)

# for numero in s1:
#     print(numero)

# Métodos úteis:
# add, update, clear, discard

# s1 = set()
# s1.add('Gabriel')#Adiciona
# s1.add(1) #Adiciona
# s1.update(('Olá Mundo', 1,2,3,4 )) #Atualiza

# s1.clear() Limpa o set

# s1.discard('Olá Mundo') #Apaga o valor que está no set
# s1.discard('Gabriel') #Apaga o valor que está no set
# print(s1)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1,2,3}
s2 = {2,3,4}

s3 = s1 | s2 # Uniao dos sets
s3 = s1 & s2 # itens que estao presentes nos sets
s3 = s1 - s2 # itens presentes apenas no set da esquerda
s3 = s1 ^ s2 # itens que não estão em ambos

print(s3)



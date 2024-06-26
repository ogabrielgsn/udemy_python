# Módulos padrão do Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html
# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes
#--PRIMEIRA MANEIRA DE IMPORTAR--
import sys
platform = 'A MINHA'
print(sys.platform)
print(platform)


# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo
# --SEGUNDA MANEIRA DE IMPORTAR--
from sys import exit, platform
print(platform)

# --TERCEIRA MANEIRA DE IMPORTAR--
# alias 1 - import nome_modulo as apelido
import sys as s
sys = 'alguma coisa'
print(s.platform)
print(sys)

# --QUARTA MANEIRA DE IMPORTAR--
# alias 2 - from nome_modulo import objeto as apelido
from sys import exit as ex
from sys import platform as pf
print(pf)

# Vantagens: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem

# má prática - from nome_modulo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo
from sys import * #Esta importando tudo do modulo

print(platform)
exit()
# Expressões Regulares - REGEX
# São padrões utilizados para selecionar combinações de caracteres em uma string.

import re # Biblioteca Regex
pattern1 = re.compile("ABC")
# Compile cria um padrão de busca
# O padrão é chamado de pattern

# Match vs Search
# Match: busca no início da string
# Search: busca em toda a string
busca1 = pattern1.match("12345 ABCDEF")
busca2 = pattern1.search("12345 ABCDEF")

# Teste com match
if busca1:
    print("Match encontrado\n")
    print(busca1.group())
else:
    print("Match não encontrado\n")

# Teste com search
if busca2:
    print("Search encontrado\n")
    print("Utilizando group -> ",busca2.group())
    print("Utilizando start -> ",busca2.start())
    print("Utilizando end -> ",busca2.end())
    print("Utilizando span -> ",busca2.span())
else:
    print("Search não encontrado\n")

# Match e Search retornam um objeto do tipo Match que possui os seguintes métodos:
# group() - retorna o texto encontrado
# start() - retorna o índice do início do texto encontrado
# end() - retorna o índice do final do texto encontrado
# span() - retorna uma tupla contendo o índice do início e do final do texto encontrado

# Metacaracteres
# . - Qualquer caractere
# [] - Conjunto de caracteres
# [^] - Conjunto de caracteres negados
# ? - Zero ou uma ocorrência
# * - Zero ou mais ocorrências
# + - Uma ou mais ocorrências
# {n} - Número exato de ocorrências
# {min, max} - Faixa de ocorrências
# () - Grupo de caracteres
# | - Ou
# \ - Caractere de escape
    
# Caracteres correspondentes
# \d - Dígitos
# \D - Não dígitos
# \s - Espaços em branco
# \S - Não espaços em branco
# \w - Alfanuméricos
# \W - Não alfanuméricos
    


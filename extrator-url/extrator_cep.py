# Utilizando Regex - Expressões Regulares

import re # Biblioteca para trabalhar com Regex

endereco = "Rua das Casas, 123, apartamento 3121, Mangueira, Floriano, PI, 64008-800"

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}") # Cria um padrão de busca 
# O padrão é chamado de pattern
busca = padrao.search(endereco) # Busca o padrão no texto

if busca: # Verifica se o padrão foi encontrado
    cep = busca.group() # Retorna o texto encontrado
    print(cep)

"""

OBS: Utilizando codificadores
"[0-9]{5}[-]{0,1}[0-9]{3}"

explicação:
[0-9]{5} - Busca 5 números
[-]{0,1} - Busca o hífen, que pode ou não existir / {0,1} = ? (opcional)
[0-9]{3} - Busca 3 números

"""
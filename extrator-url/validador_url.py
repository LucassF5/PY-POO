# Validador de URL

# Passos para criar o validador de URL:
# 1. Criar o padrão de busca
# 2. Buscar o padrão no texto
# 3. Verificar se o padrão foi encontrado

import re

url = "https://www.bytebank.com.br/cambio"
padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
# Fazendo padrão para ser comparado

match = padrao_url.match(url) # Usando match pois a url deve ser igual ao padrão
# Se fosse search, a url poderia ter mais coisas além do padrão

if not match:
    raise ValueError("A URL não é válida.")

print("A URL é válida.")
import requests

# API (Interface de Programação de Aplicações)
url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"

response = requests.get(url)

print(response) # Visualizando a resposta da url
# print(response.status_code) # Visualizando o status code da resposta

dados_restaurante = {}
if response.status_code == 200:
    dados_json = response.json() # Coletando os dados em json
    # print(dados_json)
    for item in dados_json: # Percorrendo os dados
        nome_do_restaurante = item['Company'] # Coletando o nome do restaurante
        if nome_do_restaurante not in dados_restaurante: 
            # Verificando se o nome do restaurante não está no dicionário
            # Se não estiver, adiciona o nome do restaurante como chave e uma lista vazia como valor
            dados_restaurante[nome_do_restaurante] = []

        dados_restaurante[nome_do_restaurante].append({ # Adicionando o item na lista vazia
            "item": item['Item'],
            "price": item['price'],
            "description": item['description']

        }) 

else:
    print(f"Erro {response.status_code} na requisição.")

print(dados_restaurante['McDonald’s'])

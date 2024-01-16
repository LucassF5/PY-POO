import requests
import json

url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"
response = requests.get(url)
print(response)

dados_restaurante = {}
if response.status_code == 200:
    dados_json = response.json()
    for item in dados_json: 
        nome_do_restaurante = item['Company'] 
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []

        dados_restaurante[nome_do_restaurante].append({
            "item": item['Item'],
            "price": item['price'],
            "description": item['description']
        }) 

else:
    print(f"Erro {response.status_code} na requisição.")

print(dados_restaurante['McDonald’s'])

for nome_do_restaurante, dados_do_restaurante in dados_restaurante.items():
    nome_arquivo = f"{nome_do_restaurante}.json" # Criando o nome do arquivo
    with open(nome_arquivo, "w") as arquivo: # Abrindo o arquivo
        json.dump(dados_do_restaurante, arquivo, indent=4) # Escrevendo no arquivo os dados
                #NOME DO ARQUIVO, DADOS, INDENTACAO


                # Exibindo todos os dados iterados
# for nome_do_restaurante, dados_do_restaurante in dados_restaurante.items():
#     print(f"Nome do restaurante: {nome_do_restaurante}")
#     for dados in dados_do_restaurante:
#         print(f"Item: {dados['item']}")
#         print(f"Preço: {dados['price']}")
#         print(f"Descrição: {dados['description']}")
#         print()
url = "https://bytebank.com/cambio?moedaOrigem=real&quantidade=100&moedaDestino=dolar&quantidade=100"
print(url)

"""
    Base da URL: https://bytebank.com
    /cambio é o caminho
    ? É o separador entre a base da URL e seus parâmetros
    moedaOrigem=real&moedaDestino=dolar&quantidade=100 são os parâmetros
"""


        #Separa a base da URL e os parâmetros
indice_interrogacao = url.find('?')
# O método find() retorna o índice/posição da primeira ocorrência do valor especificado.
url_base = url[0:indice_interrogacao]
# O fatiamento de string é feito da seguinte forma: string[inicio(inclusivo):fim(exclusivo):passo]
url_parametros = url[indice_interrogacao+1:]
print(url_parametros)



        #Busca o valor de um parâmetro
parametro_busca = 'quantidade' # O parâmetro que queremos buscar
indice_parametro = url_parametros.find(parametro_busca) # O índice/posição do parâmetro que queremos buscar
indice_valor = indice_parametro + len(parametro_busca) + 1 # O +1 é para pular o sinal de igual (=)
indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1: # Se não encontrar o caractere &, o índice/posição será -1
    valor = url_parametros[indice_valor:]
else: # Se encontrar o caractere &, percorre a url até o caractere &
    valor = url_parametros[indice_valor:indice_e_comercial]
print(valor)


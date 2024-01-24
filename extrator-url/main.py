url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
print(url)

"""
    Base da URL: https://bytebank.com
    /cambio é o caminho
    ? É o separador entre a base da URL e seus parâmetros
    moedaOrigem=real&moedaDestino=dolar&quantidade=100 são os parâmetros
"""

indice_interrogacao = url.find('?')
# O método find() retorna o índice/posição da primeira ocorrência do valor especificado.

url_base = url[0:indice_interrogacao]
# O fatiamento de string é feito da seguinte forma: string[inicio(inclusivo):fim(exclusivo):passo]
print(url_base)

url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

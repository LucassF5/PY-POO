class ExtratorURL:
    def __init__(self, url): # Construtor que recebe a URL
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url): # Método que limpa a URL
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self): # Método que valida a URL
        if not self.url:
            raise ValueError("A URL está vazia")

    def get_url_base(self): # Método que retorna a base da URL
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self): # Método que retorna os parâmetros da URL
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca): # Método que retorna o valor de um parâmetro
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor


extrator_url = ExtratorURL("bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)

extrator2 = ExtratorURL("https://cursos.alura.com.br/course/string-python-extraindo-informacoes-url/task/91883")
print(extrator2.get_url_base())
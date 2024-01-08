class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas

Vingadores = Filme("Vingadores - Ultimato", 2019, 180)

RickMorty = Serie("Rick and Morty", 2013, 7)

print(f"Nome: {Vingadores.nome} - Ano: {Vingadores.ano} - Duração: {Vingadores.duracao} minutos")
print(f"Nome: {RickMorty.nome} - Ano: {RickMorty.ano} - Temporadas: {RickMorty.temporadas}")
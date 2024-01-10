
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def dar_likes(self):
        self._likes += 1

    @property
    def likes(self):
        return self._likes
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f"Nome: {self._nome} - Ano: {self.ano} - {self._likes} Likes"
    
    def __repr__(self):
        print(f"__repr dentro da classe {__class__.__name__} - exibindo dentro da classe {self._nome}")
        print("Dentro do __repr__")
        return f"Nome: {self._nome} - Ano: {self.ano} - {self._likes} Likes"


class Filme(Programa): 
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano) 
        self.duracao = duracao

    def __str__(self):
        return f"Nome: {self._nome} - Ano: {self.ano} - Duração: {self.duracao} min - {self._likes} Likes"


class Serie(Programa):
    def __init__(self, nome, ano, temporadas): 
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"Nome: {self._nome} - Ano: {self.ano} - Temporadas: {self.temporadas} - {self._likes} Likes"

class Playlist: 
    def __init__(self, nome,programas):
        self.nome = nome
        self._programas = programas

    @property
    def listagem(self):
        return self._programas
    
    @property
    def tamanho(self):
        return len(self._programas)

    

vingadores = Filme("Vingadores - Ultimato", 2019, 180)
rick_morty = Serie("Rick and Morty", 2013, 7)
atlanta = Serie("Atlanta", 2018, 2)
demolidor = Serie("Demolidor", 2016, 2)

vingadores.dar_likes()
vingadores.dar_likes()
rick_morty.dar_likes()
rick_morty.dar_likes()
atlanta.dar_likes()
demolidor.dar_likes()

filmes_e_series = [vingadores, rick_morty, atlanta, demolidor]

playlist = Playlist("Fim de semana", filmes_e_series)

print(f"Tamanho da playlist: {playlist.tamanho}")

# for programa in playlist:
#     print(programa)

print(f"Está ou não está? {demolidor in playlist.listagem}") # Verificando se o objeto está na playlist
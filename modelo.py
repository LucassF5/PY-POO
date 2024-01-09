class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    
    @property
    def likes(self):
        return self.__likes
    
    def dar_likes(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()


class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    def dar_likes(self):
        self.__likes += 1

    @property
    def likes(self):
        return self.__likes
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()
        
    def mostrar_atributos(self):
        print(f"Nome: {self.__nome} - Ano: {self.ano} - Temporadas: {self.temporadas} minutos - Likes: {self.__likes}")

Vingadores = Filme("Vingadores - Ultimato", 2019, 180)

RK = Serie("Rick and Morty", 2013, 7)

print(f"Nome: {Vingadores.nome} - Ano: {Vingadores.ano} - Duração: {Vingadores.duracao} minutos - Likes: {Vingadores.likes}")
print(f"Nome: {RK.nome} - Ano: {RK.ano} - Temporadas: {RK.temporadas} - Likes: {Vingadores.likes}")
RK.nome = "rick and morty - Segunda Termporada" # alterando nome por meio do setter
RK.dar_likes()
RK.mostrar_atributos()
print(Vingadores.nome) # Verificando nome pelo getter do decorator @property
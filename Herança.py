class Programa:
    def __init__(self, nome, ano):
        # Um único _ é um atributo protegido
        #Atributos protegidos são acessados apenas pela própria classe e pelas classes filhas
        self._nome = nome.title() # Atributo protegido
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


# Para utilizar o construtor do método pai basta fazer o seguinte:
    # super().__init__(atributos do construtor do pai)
        

#Ao utilizar herança, a classe filha herda todos os atributos e métodos da classe pai
class Filme(Programa): # Herdando da classe Programa
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano) # Acessando o construtor da classe pai(que contém os atributos herdados)
        self.duracao = duracao


class Serie(Programa):
    def __init__(self, nome, ano, temporadas): # Added "duracao" argument
        super().__init__(nome, ano) # Acessando o construtor da classe pai(que contém os atributos herdados)
        self.temporadas = temporadas

Vingadores = Filme("Vingadores - Ultimato", 2019, 180)

RK = Serie("Rick and Morty", 2013, 7) # Added "duracao" argument

print(f"Nome: {Vingadores.nome} - Ano: {Vingadores.ano} - Duração: {Vingadores.duracao} minutos - Likes: {Vingadores.likes}")
print(f"Nome: {RK._nome} - Ano: {RK.ano} - Temporadas: {RK.temporadas} - Likes: {RK._likes}")
# Se duas classes possuem o mesmo pai por herança
# Pode-se utilizar polimosfismo para utilizar métodos iguais de forma diferente
# E essa classe filha pode ser utilizada como se fosse a classe pai

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

    def __str__(self):
        # __str__ é utilizado para exibir o objeto em forma de string
        return f"Nome: {self._nome} - Ano: {self.ano} - {self._likes} Likes"
    
    def __repr__(self): # Representação do objeto
        # repr() é utilizado para debugar o código, uma vez que o método __str__() é utilizado para exibir o objeto
        # uma função para desenvolvedores
        print(f"__repr dentro da classe {__class__.__name__} - exibindo dentro da classe {self._nome}")
        print("Dentro do __repr__")
        return f"Nome: {self._nome} - Ano: {self.ano} - {self._likes} Likes"


# Para utilizar o construtor do método pai basta fazer o seguinte:
    # super().__init__(atributos do construtor do pai)
        

#Ao utilizar herança, a classe filha herda todos os atributos e métodos da classe pai
class Filme(Programa): # Herdando da classe Programa
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano) # Acessando o construtor da classe pai(que contém os atributos herdados)
        self.duracao = duracao

    def __str__(self):
        return f"Nome: {self._nome} - Ano: {self.ano} - Duração: {self.duracao} min - {self._likes} Likes"
    # Sobrescrevendo o método __str__() da classe pai com sua própria assinatura


class Serie(Programa):
    def __init__(self, nome, ano, temporadas): 
        super().__init__(nome, ano) # Acessando o construtor da classe pai(que contém os atributos herdados)
        self.temporadas = temporadas

    def __str__(self):
        return f"Nome: {self._nome} - Ano: {self.ano} - Temporadas: {self.temporadas} - {self._likes} Likes"
    # Sobrescrevendo o método __str__() da classe pai com sua própria assinatura

Vingadores = Filme("Vingadores - Ultimato", 2019, 180)
RK = Serie("Rick and Morty", 2013, 7) 

playlist = [Vingadores, RK]

for programa in playlist:
    print(programa) # Forma com polimorfismo
    # O método __str__() é o mesmo para as duas classes, porém é executado de forma diferente
    # Pois cada classe possui um método __str__() diferente
    # Isso é polimorfismo

Vingadores.__repr__()
repr(RK)
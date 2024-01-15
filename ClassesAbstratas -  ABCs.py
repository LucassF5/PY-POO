# ABSTRACT BASE CLASSES - ABCs

from abc import ABC

from collections.abc import MutableSequence

class Playlist(MutableSequence): 
    # Herda de MutableSequence -> precisa/obrigado implementar os métodos abstratos
    def __init__(self) -> None:
        super().__init__() # Chama o construtor da classe herdada

# Classes abstratas não podem ser instanciadas
# Ou seja, não podemos criar objetos a partir delas
# Elas precisam ser herdadas por outras classes
# E as classes que herdarem de uma classe abstrata
# precisam implementar seus métodos abstratos

# Para criar uma classe abstrata, basta herdar de ABC
# e decorar os métodos abstratos com @abstractmethod
# e os atributos abstratos com @abstractattribute

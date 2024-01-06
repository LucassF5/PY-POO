
class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    @property
    # O @property é um decorator que permite que um método seja chamado como se fosse um atributo
    # Ou seja, usa o método como se fosse um atributo
    def nome(self):
        # Getter
        print("Chamando @property nome()")
        return self.__nome.title()
    
    @nome.setter
    # O @nome é um decorator que permite que um método seja chamado como se fosse um atributo
    def nome(self, nome):
        # Setter
        print("Chamando @nome.setter nome()")
        self.__nome = nome


cliente = Cliente("lucas franco")

print("\n",cliente.nome,"\n") #Utilizando getter
# Utiliza-se como se fosse um atributo
# Não precisa de parenteses

cliente.nome = "maria" #Utilizando setter
print("\n",cliente.nome) #Novamente utilizando getter
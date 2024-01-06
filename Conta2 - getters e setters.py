
class Conta:
    def __init__(self, numero, titular, saldo, limite): 
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"Saldo de {self.__saldo} do titular {self.__titular}")

    # Métodos Getters e Setters
        # Getters são métodos que retornam o valor de um atributo
        # Setters são métodos que alteram o valor de um atributo

    def get_saldo(self):
        return self.__saldo
    def set_saldo(self, saldo):
        self.__saldo = saldo
    

    def get_titular(self):
        return self.__titular
    
    
    def get_limite(self):
        return self.__limite
    def set_limite(self, limite):
        self.__limite = limite


    @staticmethod # Método estático
    # Método estático é um método da classe
    # Não precisa criar um objeto para acessar o método
    def codigo_banco():
        return "001"
    

conta = Conta(100, "Lucas", 150.0, 1000.0)
conta.set_saldo(200.0)
print("O limite atual é:",conta.get_saldo())

print(Conta.codigo_banco()) 
# Não é necessário uma instância da classe para chamar um método estático

## Utilizando o @property na classe Conta

#     @property
#     def saldo(self):
#         return self.__saldo
#     @saldo.setter
#     def saldo(self, saldo):
#         self.__saldo = saldo
    
#     @property
#     def titular(self):
#         return self.__titular
    
#     @property
#     def limite(self):
#         return self.__limite
#     @limite.setter
#     def limite(self, limite):
#         self.__limite = limite

# conta = Conta(100, "Lucas", 150.0, 1000.0)
# conta.saldo = 200.0
# print("O limite atual é:",conta.saldo)

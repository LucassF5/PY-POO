
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

conta = Conta(100, "Lucas", 150.0, 1000.0)
conta.set_saldo(200.0)
print("O limite atual é:",conta.get_saldo())

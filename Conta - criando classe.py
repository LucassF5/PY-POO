

class Conta:
    
    # construtor da classe -> __init__
    def __init__(self, numero, titular, saldo, limite): 
        #dentro dos parênteses são os parâmetros do construtor, atributos da classe

        # self é uma referência na memória para o objeto que está sendo criado
        print("Construtor da classe Conta, {}\n".format(self))
        # Atributos com dois underlines são privados
        # Atrinutos privados não podem ser acessados diretamente
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    # Iniciando métodos da classe
    def extrato(self):
        # Todo método é uma função
        # Todo método deve ter o self como parâmetro
        print(f"Saldo de {self.__saldo} do titular {self.__titular}")

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar): # método privado
        valor_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
            print(f"Saque de {valor} reais realizado com sucesso\n")
        else:
            print(f"O valor {valor} passou o limite")

    def transfrere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
        print(f"{self.__titular} transferiu {valor} reais para {destino.__titular}\n")

    # def mostra_tudo(self):
    #     print(f"Número: {self.numero} \nTitular: {self.titular} \nSaldo: {self.saldo} \nLimite: {self.limite}")



conta = Conta(100, "Lucas", 150.0, 1000.0)
conta2 = Conta(101, "Maria", 100.0, 1000.0)
#  conta é uma referência para o objeto do tipo Conta
# print(conta.titular, "é o titular da conta")
# Utilizando NomeDaClasse.atributo, é possível acessar o atributo da classe

conta.extrato()
conta2.extrato()
# Utilizando NomeDaClasse.método, é possível acessar o método da classe

conta.transfrere(50, conta2)
conta.extrato()
conta2.extrato()

conta.saca(2000)
conta.saca(200)
conta.extrato()
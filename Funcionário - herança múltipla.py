# Herança múltipla

# Com herança múltipla, uma classe pode herdar de várias classes
# E assim, herdar todos os seus comportamentos

class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print('Horas registradas...')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario): # Herda de Funcionario
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Alura(Funcionario): # Herda de Funcionario
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')

class Junior(Alura): # Herda de Alura
    
    def mostrar_tarefas(self):
        # Sobrescrevendo método da classe mãe
        print('Fez muita coisa', __class__.__name__)

class Pleno(Alura, Caelum): # Herda de Alura e Caelum
    
    def mostrar_tarefas(self):
        # Sobrescrevendo método da classe mãe
        print('Fez muita coisa', __class__.__name__)

class Senior(Alura, Caelum): # Herda de Alura e Caelum
    
    def mostrar_tarefas(self):
        # Sobrescrevendo método da classe mãe
        print('Fez muita coisa', __class__.__name__)

#Classe MIXIN
# Uma classe que não depende de outra classe
# para funcionar, mas que pode estender
# o comportamento de/para outra classe
class Hipster:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f'Hipster, {self.nome}'

Lucas = Junior("Lucas")
Lucas.mostrar_tarefas()
#Usando o método mostrar_tarefas da classe Junior
Lucas.busca_perguntas_sem_resposta()
# Usando o método mostrar_tarefas da classe Alura

Maria = Pleno("Maria")
Maria.busca_perguntas_sem_resposta()
# Usando o método mostrar_tarefas da classe Alura
Maria.busca_cursos_do_mes()
# Usando o método busca_cursos_do_mes da classe Caelum
Maria.mostrar_tarefas()
# Usando o método mostrar_tarefas da classe Pleno
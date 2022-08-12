class Calculadora:
    def __init__(self):
        self.__registrador = 0
        self.__qtde_operacoes = -1
        self.historico = []

    @property
    def registrador(self):
        return self.__registrador

    @registrador.setter
    def registrador(self, valor):
        self.__registrador = valor

    @property
    def qtde_operacoes(self):
        return self.__qtde_operacoes

    @qtde_operacoes.setter
    def qtde_operacoes(self, valor):
        self.__qtde_operacoes = valor

    def somar(self, valor):
        self.historico.append(self.registrador)
        self.registrador += valor
        self.qtde_operacoes += 1

    def subtrair(self, valor):
        self.historico.append(self.registrador)
        self.registrador -= valor
        self.qtde_operacoes += 1

    def dividir(self, valor):
        self.historico.append(self.registrador)
        self.registrador /= valor
        self.qtde_operacoes += 1

    def multiplicar(self, valor):
        self.historico.append(self.registrador)
        self.registrador *= valor
        self.qtde_operacoes += 1

    def resetar(self):
        self.historico.append(self.registrador)
        self.registrador = 0
        self.qtde_operacoes += 1

    def exibe_registrador(self):
        print(self.registrador)

    def desfazer(self):
        self.registrador = self.historico[self.qtde_operacoes]

    def sair(self):
        return 'sair'

    

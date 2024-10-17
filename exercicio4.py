from abc import ABC, abstractmethod

class ContaBancaria(ABC):
    def __init__(self, numero_conta, titular, saldo=0):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo

    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def sacar(self, valor):
        pass

    def getData(self):
      print(f"O {self.titular} da conta {self.numeroconta} tem o saldo de {self.saldo} reais")

class Contacorrente(Contabancaria):
  def __init__(self,numeroconta,titular,saldo,limite):
    super().__init__(numeroconta,titular,saldo)
    self.limite = limite

  def sacar(self,valor):
    if (self.saldo + self.limite) < valor:
      print("Saldo insuficiente /vc esta na conta corrente cheque especial")
    else:
      self.saldo -=valor

class Contapoupanca(Contabancaria):
  def __init_self(self,numeroconta,titular,saldo,taxa_juros):
    super().__init__(numeroconta,titular,saldo,)

  def sacar(self,valor):
    if self.saldo < valor:
      print("Saldo insuficiente/vc esta na conta poupanca e nao pode sacar alem do saldo")
    else:
      self.saldo -= valor

  def calcular_juros(self):
        self.saldo += self.saldo * self.taxa_juros / 100

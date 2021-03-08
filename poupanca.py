from conta import Conta

class Poupanca(Conta):

  juros_ao_mes = 0.0

  def __init__(self, numero, agencia):
    super().__init__(numero, agencia)
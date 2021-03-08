from conta import Conta

class Corrente(Conta):

  limite = 0.0

  def __init__(self, numero, agencia):
    super().__init__(numero, agencia)

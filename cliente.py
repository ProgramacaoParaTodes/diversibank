from usuarie import Usuarie
from endereco import Endereco
from corrente import Corrente
from poupanca import Poupanca

class Cliente(Usuarie):

  endereco = Endereco()
  contas = []

  def __init__(self, cpf, nome, email, celular, renda):
    super().__init__(cpf, nome, email, celular)
    try:
      self.renda = float(renda)
    except ValueError:
      self.renda = 0.0
      print("Atenção! Renda inválida!")   

  def adicionar_conta(self, conta):
    self.contas.append(conta)
from usuarie import Usuarie

class Gerente(Usuarie):

  pessoa_fisica = True
  pessoa_juridica = False

  def __init__(self, cpf, nome, email, celular):
    super().__init__(cpf, nome, email, celular)
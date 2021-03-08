from cliente import Cliente
from gerente import Gerente
from corrente import Corrente
from poupanca import Poupanca
from endereco import Endereco
import util

# teste = Cliente("123.123.123-00", "Teste", "teste@teste.com", "(21)999121212", 5000.0)

# endereco_teste = Endereco()
# endereco_teste.logradouro = "Rua das Flores"
# endereco_teste.numero = "15 Fundos"
# endereco_teste.bairro = "Centro"
# endereco_teste.cidade = "Rio de Janeiro"
# endereco_teste.uf = "RJ"
# endereco_teste.cep = "12345-000"

# if util.valida_sigla_estado(endereco_teste.uf):
#   teste.endereco = endereco_teste

# print(teste.endereco.uf)

clientes = []

while True:

  print("----- DiversiBank -----")
  print("[A]dicionar")
  print("[E]ditar")
  print("[D]eletar")
  print("[V]isualizar todes")
  print("[C]riar conta corrente")
  print("[S]air")

  op = input("Digite uma opção: ")

  if op.upper() == "A":
    # cpf, nome, email, celular, renda
    cpf = input("Digite o CPF: ")
    nome = input("Digite o nome: ")
    email = input("Digite o email: ")
    celular = input("Digite o celular: ")
    renda = input("Digite a renda: ")

    # MELHORIA: verificar na lista de clientes se já existe um cliente com aquele CPF cadastrado

    # TODO: implementar try / exception
    novo_cliente = Cliente(cpf, nome, email, celular, float(renda))
    clientes.append(novo_cliente)
  
  elif op.upper() == "E":
    print("Editar")
  elif op.upper() == "D":
    print("Deletar")
  elif op.upper() == "V":
    # TODO: tratar lista de clientes vazia
    posicao = 0
    for cliente in clientes:
      print("%d: %s - %s" % (posicao, cliente.cpf, cliente.nome))
      posicao += 1
  elif op.upper() == "C":
    # TODO: tratar lista de clientes vazia
    posicao = 0
    for cliente in clientes:
      print("%d: %s - %s" % (posicao, cliente.cpf, cliente.nome))
      posicao += 1

    cliente_escolhido = input("Digite o número do cliente: ")

    cliente = clientes[int(cliente_escolhido)]

    # criar a conta 
    conta = Corrente("00001-0", "1")    # melhoria: controlar o número da conta

    # atrelar a conta ao cliente -> USANDO NOSSO MÉTODO
    cliente.adicionar_conta(conta)

    # sobrescrever esse cliente na lista de clientes
    clientes.insert(int(cliente_escolhido), cliente)

  elif op.upper() == "S":
    break
  else: 
    print("Opção inválida!")

def valida_sigla_estado(uf):
  UFs = ("AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO")
  # procurar um objeto dentro de uma tupla
  # neste caso, o objeto é uf, que é uma string
  if uf in UFs:
    return True
  else:
    return False

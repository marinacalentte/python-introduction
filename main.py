from datetime import date

def introducao_pessoal(nome, idade):
  print("ola, eu sou ", nome, " e tenho ", idade, " anos")

def calcular_idade(data_nascimento):
  today = date.today()
  return today.year - data_nascimento.year - ((today.month, today.day) < (data_nascimento.month, data_nascimento.day))

introducao_pessoal("andre", 37)
introducao_pessoal("marina", 35)
introducao_pessoal("bento", 4)

print(calcular_idade(date(1982, 7, 6)))

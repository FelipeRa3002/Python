#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M -
#Masculino, Sexo Inválido.
x=True
while x:
  resposta = input("Diga qual é o seu sexo, M ou F:")
  resposta=resposta.upper()
  if resposta == "M":
    print("Você é do sexo masculino")
    x=False
  elif resposta == "F":
    print("Você é do sexo feminino")
    x=False
  else:
    print("Porfavor digite novamente o seu sexo, M ou F")
            
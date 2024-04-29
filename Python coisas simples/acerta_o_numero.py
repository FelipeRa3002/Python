import random
a=1
#O limite possível que random pode escolher tipo de 1 até x, vai ser a variável b
b=int(input("Digite um número inteiro para ser o limite possível, exemplo de 1 á 10 você deve digita \"10\" sem as aspas: "))
#Seu número escolhido vai ser a variável n
n=int(input("Digite um número inteiro: "))
#Número do escolhido pelo o random vai ser a variável r
r=random.randint(a,b)
#Número de tentativa vai ser a variável c
c=1
if n==r:
    print(f"Você ganhou!!! em {c} tentativa")
else:
    controle=True
    while controle:
        c=c+1
        if n>r:
                print("O número escolhido é menor")
        elif n<r:
                print("O número escolhido é maior")
        n=int(input("Digite um número inteiro: "))
        if n==r:
            print(f"Você ganhou!!! em {c} tentativa") 
            controle=False
        
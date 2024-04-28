#7. Faça um Programa que leia três números e mostre o maior e o menor deles.
n1 = float(input("Digite o primeiro número:"))
n2 = float(input("Digite o segundo número:"))
n3 = float(input("Digite o terceiro número:"))
#Maior
if n1 > n2 and n1 > n3 or n1 > n2 and n1 == n3 or n1 == n2 and n1 > n3 or n1 == n2 and n1 == n3:
  maior = n1
elif n2 > n1 and n2 > n3 or n2 > n1 and n2 == n3 or n2 == n1 and n2 > n3 or n2 == n1 and n2 == n3:
    maior = n2
elif n3 > n1 and n3 > n2 or n3 > n1 and n3 == n2 or n3 == n1 and n3 > n2 or n3 == n1 and n3 == n2:
    maior = n3
#Menor
if n1 < n2 and n1 < n3 or n1 < n2 and n1 == n3 or n1 == n2 and n1 < n3 or n1 == n2 and n1 == n3:
 menor = n1
elif n2 < n1 and n2 < n3 or n2 < n1 and n2 == n3 or n2 == n1 and n2 < n3 or n2 == n1 and n2 == n3:
    menor = n2
elif n3 < n1 and n3 < n2 or n3 < n1 and n3 == n2 or n3 == n1 and n3 < n2 or n3 == n1 and n3 == n2:
    menor = n3
print("O maior número é {:.2f} e O menor número é {:.2f}".format(maior,menor))

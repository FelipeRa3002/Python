#9. Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 = float(input("Digite o primeiro número:"))
n2 = float(input("Digite o segundo número:"))
n3 = float(input("Digite o terceiro número:"))
if n1 > n2 and n1 > n3:
    if n2 > n3:
        print(f"A ordem descrescente dos números que você digitou é {n1} ; {n2} ; {n3}")
    else:
         print(f"A ordem descrescente dos números que você digitou é {n1} ; {n3} ; {n2}")  
elif n2 > n1 and n2 > n3:
    if n1 > n3:
        print(f"A ordem descrescente dos números que você digitou é {n2} ; {n1} ; {n3}")
    else:
         print(f"A ordem descrescente dos números que você digitou é {n2} ; {n3} ; {n1}")
elif n3 > n1 and n3 > n2:
    if n1 > n2:
       print(f"A ordem descrescente dos números que você digitou é {n3} ; {n1} ; {n2}")
    else:
       print(f"A ordem descrescente dos números que você digitou é {n3} ; {n2} ; {n1}") 
else:
    print("Os números que você digitou são os mesmos")     
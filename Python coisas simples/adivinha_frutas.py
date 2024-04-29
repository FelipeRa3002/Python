import random
import os
opcao=["MAÇÃ","BANANA","UVA","LARANJA","ABACATE",'AMORA','AMEIXA','ACEROLA','ABACAXI']
#tamanho da lista vai ser o a também.
b=1
a=0
for x in opcao:
    print(x)
    a=a+1
x=random.randint(b,a)
#A opção escolhida vai ser defina embaixo dessa linha.
opcaoe=opcao[x]
tentativa=1
voce=str(input("Qual dessas frutas você achar que o computador escolheu: "))
voce=voce.upper()
if voce=="MACA" or voce=="MACÃ" or voce=="MAÇA":
    voce="MAÇÃ"
if voce==opcaoe:
    print(f"Acertou!!!! em {tentativa} tentativa(s)")
else:
    #controle do loop vai ser c
    c=True
    while c:
        os.system('cls')
        tentativa=tentativa+1
        opcao.remove(voce)
        for x in opcao:
            print(x)
        voce=str(input("Você errou.Vamos tentar novamente,qual dessas frutas você achar que o computador escolheu: "))
        voce=voce.upper()
        if voce=="MACA" or voce=="MACÃ" or voce=="MAÇA":
            voce="MAÇÃ"
        a=a-1
        
        if voce==opcaoe:
            print(f"Acertou!!!! em {tentativa} tentativa(s)")
            c=False
        elif a==2:
            print("Você perdeu")
            c=False

    


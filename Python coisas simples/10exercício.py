#10. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N-
#Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
import os
y=0
x = True
while x:
    turno = str(input("Digite qual é o seu turno, M para matutino ou V para vespertino ou N para Noturno: "))
    turno=turno.upper()
    if turno == "M":
         print("Tenha um bom dia !!!")
         x=False
    elif turno == "V":
           print("Tenha uma boa tarde !!!")
           x=False
    elif turno == "N":
           print("Tenha uma boa noite !!!")
           x=False
    else:
            print("Valor Inválido, por favor digite o seu turno novamente !!!")
            y=y+1
            c=y%3
            if c==0:
                os.system('cls')

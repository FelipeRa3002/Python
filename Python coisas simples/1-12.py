x=False
while x==False:
 n = str(input('Seu nome: ')).capitalize()
 x=n.isalpha()
a = float(input('Qual é a sua altura: '))
p = float(input('Qual é o seu peso: '))
pi = (72.7 * a) - 58
if p == pi:
    print('Olá {:=^20} ,você tem {:.2f} de altura e {:.2f} de peso que é igual ao seu peso ideal'.format(n, a, p))
if p > pi:
    print('Olá {:=^20} ,você tem {:.2f} de altura e {:.2f} de peso que é maior que {:.2f} que é o seu peso ideal'.format(n, a, p, pi))
else :
    print('Olá {:=^20} , você tem {:.2f} de altura e {:.2f} de peso que é menor que {:.2f} que é o seu peso ideal'.format(n, a, p, pi ))
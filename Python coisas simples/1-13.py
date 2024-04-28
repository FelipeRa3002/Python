o = str(input('Você quer usa esse programa em EN ou em PT BR? ').upper())
x=False
if o == 'EN' or o == 'E':
    while x==False:
      n = str(input('Your name: ').capitalize())
      x=n.isalpha()

    s = str(input('What is your gender: ').capitalize())
    s= s.upper()
    a = float(input('What is your height: '))
    if s == 'MAN' or s == 'M':
        pi = (72.7*a) - 58
        print('{} your ideal weight is {:.2f}'.format(n , pi))
    else:
        pi = (62.1*a)-44.7
        print('{} your ideal weight is {:.2f}'.format(n, pi))
else:
    while x==False:
     n = str(input('Qual é o seu nome: ').capitalize())
     x= n.isalpha()
    s = str(input('Qual é o seu sexo: ').capitalize())
    s= s.upper()
    a = float(input('Qual é a sua altura: '))
    if s=='HOMEM' or s=='H':
        pi = (72.7 * a) - 58
        print('{} o seu peso ideal é de {:.2f}'.format(n, pi))
    else:
        pi = (62.1 * a) - 44.7
        print('{} o seu peso ideal é de {:.2f}'.format(n, pi))
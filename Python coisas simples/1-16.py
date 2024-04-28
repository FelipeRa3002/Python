a = float(input('Quantos metros quadrados vai ser pintada: '))
p = 80.0
t = (a/3)/18
if t == 1 :
    print('Você vai precisa de {:.1f} lata de tinta e vai sair por R$ {:.2f}'.format(t, t * p))
else:
   f = (a/3)//18
   if f == t:
       print('Você vai precisa de {:.1f} latas de tintas e vai sair por R$ {:.2f}'.format(t, t * p))
   else:
        print('Você vai precisa de {:.1f} latas de tintas e vai sair por R$ {:.2f}'.format(t, t * p))
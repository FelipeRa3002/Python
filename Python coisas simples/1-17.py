a = float(input('Quantos metros quadrados vai ser pintada: '))
p = 80.0
p2 = 25.0
r = str(input('Você vai compra somente lata(s): ').capitalize())
if r == 'Sim' or r == 'S' or r == 'Yes' or r == 'Y':
    t = (a/6)/18
    if t == 1:
        print('Você vai precisa de {:.1f} lata de tinta e vai sair por R$ {:.2f}'.format(t, t * p))
    else:
        f = (a / 6) // 18
        if f == t:
            print('Você vai precisa de {:.1f} latas de tintas e vai sair por R$ {:.2f}'.format(t, t * p))
        else:
            print('Você vai precisa de {:.1f} latas de tintas e vai sair por R$ {:.2f}'.format(t, t * p))
else:
    r = str(input('Você vai compra somente galões: ').capitalize())
    if r == 'Sim' or r == 'S' or r == 'Yes' or r == 'Y':
        t = (a / 6) / 3.6
        if t == 1:
            print('Você vai precisa de {:.1f} galão de tinta e vai sair por R$ {:.2f}'.format(t, t * p2))
        else:
            f = (a / 6) // 3.6
            if f == t:
                print('Você vai precisa de {:.1f} galões de tintas e vai sair por R$ {:.2f}'.format(t, t * p2))
            else:
                print('Você vai precisa de {:.1f} galões de tintas e vai sair por R$ {:.2f}'.format(t, t * p2))
    else:
        gq = float(input('Quantos galõe(s) vai ser: '))
        lq = float(input('Quantos lata(s) vai ser: '))
        pg = gq * p2
        pl = lq * p
        ta = (((pg+pl)*10)/100)+pg+pl
        print('Vai ser {:.1f} lata(s) e {:.1f} galões que vai sair por R$ {:.2f} \nAviso cada litro é seis metros quadrados,ou seja , uma lata é 108 metros quadrados e um galão é 21.6 metros quadrados'.format(lq, gq,ta))


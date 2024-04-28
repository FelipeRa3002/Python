p = float(input('Olá João pescador, quantos kilos(quilos) de peixe você pegou: '))
SP = 50.0
pa = p - SP
if p > SP :
    m = pa * 4.0
    print('Você tem {:.2f} a mais do que o limite então você vai pagar R$ {:.2f} de multa'.format(pa , m))
elif p == SP:
    print("Você pegou o limite permitido,que sorte pois você não vai precisa pagar a multa")
else:
    print('Você não passou do limite')


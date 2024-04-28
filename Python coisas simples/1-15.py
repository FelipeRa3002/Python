g = float(input('Quanto você ganha por hora: '))
m = int(input('Quantas horas você faz por mês: '))
s = g * m
d = (s*11)/100
sl = s - d
n = (s*8)/100
c = (s*5)/100
print('O seu salário bruto é de R$ {:.2f} \nMas com o desconto do INSS que é de R$ {:.2f} \nE do sindicato que é de R$ {:.2f} \nTotal de desconto é de R$ {:.2f} \nO seu salário líquido é de R$ {:.2f}'.format(s, n, c, n+c, sl ))
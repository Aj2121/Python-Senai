# abaixo 200m = 0,20$
# entre 200m e 400m 0,18
# acima de 400m 0,15$

min = int(input('digite a quantidade de minutos ultilizados no mes'))
if min < 200:
    preco = 0.20
if min < 400:
    preco = 0.18
else:
    preco = 0.15
print('voce vai pagar este mês: R$%6.2f'(min * preco))

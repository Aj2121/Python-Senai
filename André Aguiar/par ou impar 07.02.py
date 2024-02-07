import random
ptsusuario = ptscoputador = 0
while True:
    n = int(input('qual numero entre 0 a 10?'))
    parouimpar = input('par ou impar?  responda: p/1')
    while parouimpar != 'p' and parouimpar != '1':
        parouimpar = input('resposta invalida? respondap/1')
    computador = random.randit(0,10)
    soma = n + computador
    if soma %2 == 0 and parouimpar =='p':
        ptsusuario +=1
    elif soma %2 == 1 and parouimpar == '1':
        ptsusuario += 1
    else:
        ptscoputador += ptscoputador
        break
print (f'você venceu {ptsusuario} partidas')
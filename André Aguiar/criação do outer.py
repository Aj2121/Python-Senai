#criaçao do outer for loop
for numero1 in range(5):
    print(numero1)
    #criaçao do outer for loop
    for numero1 in range(5):
        print(numero1)

for numero1 in range(1,5):
    print('produto', str(numero1))
    #criaçao do outer for loop
    for numero2 in range(5):
        print(numero1,numero2)

palavra = 'FANTASTICO'
#DECLARAÇÃO FOR
for spaco in palavra:
    print(spaco, end = '')
#end vai impedir da palavra de pular linha
linha = 6
colunas = 6
simbolo = '@'
for i in range(linha):
    for c in range(colunas):
        print(simbolo)

soma = cont = 0
while True:
    n = int(input('digite um numero: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'você somou {cont} numeros')
print(f'a soma de todos foi {soma}')
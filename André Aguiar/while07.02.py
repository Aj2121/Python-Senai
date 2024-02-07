'''resp = input('Deseja iniciar o programa? s/n')
while resp == 'n':
    resp = input('resposta invalida!!! continuar? s/n')
if resp == 's':
    print('resposta ok. vamos continuar')
    print('Fim do programa')


n = int(input('digite um valor, ira parar no 999'))
soma = 0
while n!= 999:
    soma += n
    n = int(input('Digite outro numero para ser somado com os anteriores: 999 - para sair'))
print(f'soma = {soma}')

senha = '414238'
leitura = ' '
while (leitura != senha):
    leitura = input('Digite a senha:')
if leitura == senha:
    print('Acesso liberado')
else:
    print('Senha incorreta.tente novamente')

qtde = int(input('quantos termos do fibonaci voce deseja?'))
anterior = 0
atual = 1
contador = 1
while contador <= qtde:
    print('{} -', format (atual), end = ' ')
    proximo = anterior + atual
    anterior = atual
    atual = proximo
    contador += 1
print('fim do programa de fibanacci')
print(contador)
'''

soma = 0
qtdenumeros = 1
resp = 's'
while resp == 's':
    n = int(input('digite um numero: '))
    if qtdenumeros == 1:
        maior = n
        menor = n 
    if n > n:
        maior = n
    if n < menor:


'''nome = str(input('Digite seu Nome'))
email = input('Digite seu email')
ender = input('Digite seu endereço')
tel = int(input('Digite seu telefone'))
cpf = int(input('Digite seu Cpf'))
car = int(input('Digite os numeros do seu cartão de credito'))
cod = int(input('Digitre o Codigo de Segurança'))
print(nome,email  )
n1 = str(input('Deseja efetuar a Compra sim/não?'))
if n1 == 'sim':
    print('Dados Roubados com Sucesso')
else:
    print('Falha na Compra')'''

compra_confirmada = True
dados_compra = 'compra no valor de R$12.,50 e entrega confirmada'
#melhorando op for
#break usado para parar o contigo
for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('Delathes enviado para o seu email')
        break
else:
    print('Falha na compra')

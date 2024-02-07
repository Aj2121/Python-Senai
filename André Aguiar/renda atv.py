renda = int(input('de quando é a sua renda'))
nome = str(input('seu nome esta limpo'))
if renda >= 5000 or nome == 'sim':
    print('Voce pode financiar')
else:
    print('Você não pode financiar')

valor = int(input('qual valor do seu produto'))
if valor >= 20 and valor < 40:
    print('pode publicar')
else:
    print('valor não esta nas diretrizes do site')

n1 = float(input('digite a nota do aluno'))
n2 = float(input('digite a nota do aluno'))
n3 = float(input('digite a nota do aluno'))
n4 = float(input('digite a nota do aluno'))
media = (n1 + n2 + n3 + n4) / 4
if media >= 6:
    print(f'Aprovado{media:.1f}')
elif media >=3 and media <6:
    print(f'Exame {media:.1f}')
else:
    print(f'Reprovado{media:.1f}')








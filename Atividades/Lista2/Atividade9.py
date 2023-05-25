n1 = float(input('Qual a sua 1 nota? '))
n2 = float(input('Qual a sua 2 nota? '))
n3 = (n1+n2)/2

if n3>=9:
    conceito = 'A'
elif n3>=7.5:
    conceito = 'B'
elif n3>=6:
    conceito = 'C'
elif n3>=4:
    conceito = 'D'
else:
    conceito = 'E'

print (f'Sua primeira nota foi {n1}, sua segunda nota foi {n2}, e a média entre elas é {n3}')
print(conceito)

if conceito in ['A', 'B', 'C']:
    print('APROVADO')
else:
    print('REPROVADO')
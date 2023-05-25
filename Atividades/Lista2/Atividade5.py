n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

if n1>n2:
    print(f'{n1} é o maior número')
elif n2>n1:
    print(f'{n2} é o maior número')
else:
    print('Os números não podem ser iguais')
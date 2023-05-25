n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

if n1>n2:
    print(f'{n1}, {n2}')
elif n2>n1:
    print(f'{n2}, {n1}')
else:
    print('Os números não podem ser iguais')
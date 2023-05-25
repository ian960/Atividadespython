n1 = float(input('Qual o número da sua conta? '))
n2 = float(input('Qual o saldo da sua conta?'))
n3 = float(input('Qual o débito da sua conta?'))
n4 = float(input('Qual o crédito da sua conta?'))
n5 = n2-n3+n4

print (f'Seu saldo atual é: {n5}')

if n5<0:
    print('Saldo negativo')
else:
    print('Saldo positivo')
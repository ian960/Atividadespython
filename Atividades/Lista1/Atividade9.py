n1 = float(input('Qual a sua altura? '))
s1 = input('Qual o seu gênero? (M para masculino / F para feminino)')

if s1 == ('M'):
    print (f'Seu peso ideal é {(n1*72.7) - 58}')
elif ('F'):
    print (f'Seu peso ideal é {(n1*62.1) - 44.7}')
else:
    print ('Gênero invalido')
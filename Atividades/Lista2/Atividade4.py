n1 = float(input('Qual é a sua primeira nota? '))
n2 = float(input('Qual é a sua segunda nota? '))
media = (n1 + n2) / 2

if media < 6:
    print(f'Você tirou {media}, infelizmente foi reprovado')
else:
    print(f'Parabéns! Sua nota foi {media}, você foi aprovado')

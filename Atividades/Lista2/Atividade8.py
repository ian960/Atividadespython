n1 = int(input('Quantas cervejas tem na geladeira? '))
n2 = int(input('Quantas cervejas cabem na geladeira? '))
n3 = int(input ('Quantas cervejas tenho que deixar na geladeira?'))
n4 = (n2+n3)/2

if n1>=n4:
    print('Não compre mais cerveja :( ')
else:
    print('Vá comprar cerveja!')

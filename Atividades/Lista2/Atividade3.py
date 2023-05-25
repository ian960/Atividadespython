n1 = float(input('As maçãs custam 1,30 cada, se forem compradas menos de uma dúzia, e 1,00 se forem compradas pelo menos 12. Quantas maçãs você quer?'))
if n1<12:
    print(f'Total igual à: {n1*1.30} reais')
else:
    print(f'Total igual à: {n1} reais')
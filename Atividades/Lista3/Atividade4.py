numero = int(input("Digite um número para a tabuada: "))

print("Tabuada do número", numero)
for i in range(1, 11):
    print(numero, "x", i, "=", numero*i)

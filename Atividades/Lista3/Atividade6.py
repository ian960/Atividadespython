# a) Lista de convidados
convidados = ["Michelle Obama", "Beyoncé", "Elon Musk", "Emma Watson", "Chris Evans"]

# b) Envio dos convites
mensagem = "Olá, você está convidado para um jantar em minha casa na próxima sexta-feira às 20h. Espero vê-lo lá!"
for convidado in convidados:
    print("Enviando convite para:", convidado)
    print(mensagem.replace("vê-lo", "vê-la" if convidado == "Emma Watson" else "vê-lo").replace("!", ", " + convidado + "!"))

# c) Lidando com desistências
desistentes = ["Emma Watson"]
for desistente in desistentes:
    print(desistente, "não poderá comparecer ao jantar.")

# d) Substituindo desistentes por novos convidados
convidados.remove(desistentes[0])
convidados.append("Tom Hanks")
print("Emma Watson foi substituída por Tom Hanks na lista de convidados.")

# e) Novos convites para os presentes
for convidado in convidados:
    print("Enviando novo convite para:", convidado)
    print(mensagem.replace("vê-lo", "vê-la" if convidado == "Emma Watson" else "vê-lo").replace("!", ", " + convidado + "!"))

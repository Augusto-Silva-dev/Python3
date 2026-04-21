proibidas = ["spam", "fraude", "golpe"]
palavra = "fraude"

if len(palavra) > 5:
    if palavra not in proibidas:
        print("Palavra aceita!")
    else:
        print("Palavra proibida!")
else:
    print("Palavra muito curta!")
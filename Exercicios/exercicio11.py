proibidos = ['spam', 'golpe', 'fraude'] #lista proibida
itens = ['laranja', 'spam', 'uva'] #lista de itens (permitida)

for item in itens: #função para determinar exclusivamente a busca em "itens"
    if len(item) > 3:
        if item not in proibidos: #Se o item não estiver em em proibidos e o número de letras for maior que 3 ele é válido
            print(f'{item}: Válido!')
        else: #Se o item tiver mais do que 3 letras e estiver em "proibidos" ele é proibido
            print(f'{item}: Proibido!')
    else: #Do contrário das 3 afirmações acima, ele é curto
        print(f'{item}: Muito curto!')
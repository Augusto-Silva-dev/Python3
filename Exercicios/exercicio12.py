lista = ['azul', 'vermelho', 'verde'] #Lista

try:
    if len(lista) == 0: #Contagem da lista (O índice começa em 0)
        print('A lista está vazia!')
    else:
        print(f'Primeiro: {lista[0]}') #Retorne o primeiro da lista
        print(f'Último: {lista[-1]}') #Retorne o último da lista (função para retornar o contrário)
except:
    print('Erro inesperado!') #Se tudo der errado, retorne isso
#Somatório utilizando lista e while


number = [1, 2, 3, 4] #lista pré definida

print(f'{number}')

calc = int( input('Escolha um número da lista para começarmos:')) #pede ao usuário escolher um número da lista


while calc:

    if calc in number: #enquanto calc = True e o número escolhido estiver na lista, continue o programa
        
        print(f'O valor é {calc + 1}') #resultado final da lista
        
        break

    else: #caso não digite o valor da lista, peça ao usuário que reescreva o valor correto
        print('Você não digitou um número') 
        calc = int (input('Por favor, digite um valor correto que esteja na lista:')) 
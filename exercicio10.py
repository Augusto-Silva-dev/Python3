lista = ['maçã', 'banana', 'uva']
entrada = '1'

try:
    indice = int(entrada)
    print(f'O item é: {lista[indice]}')
except ValueError:
    print('Digite apenas números!')
except:
    print('Índice fora da lista!')
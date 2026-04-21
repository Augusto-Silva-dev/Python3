numeros = [2, 5, 8, 13, 20]
numero = 8

if numero in numeros:
    if numero % 2 == 0:
        print(f'{numero} está na lista e é par!')
    else:
        print(f'{numero} está na lista e é ímpar!')
else:
    print(f'{numero} não está na lista!')
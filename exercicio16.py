"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = float(input('Olá, digite um número:')) #pede ao usuário um número

if (numero % 2 == 0): #vai descobrir se é par ou ímpar
    print('Este número é par')
else:
    print('Este número não é par')
if (numero == int(numero)):
    print('É inteiro')
else:
    print('Não é inteiro')
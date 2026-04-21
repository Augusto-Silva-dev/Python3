n=str(input('Olá, por favor digite seu nome:'))
acesso=input(f'Olá, {n}! Seja bem vindo, você deseja entrar ou sair?')
senha_permitida= '1921'
senha=input('Por favor, digite a senha:')
if (acesso == 'Entrar' or acesso == 'entrar') and senha==senha_permitida:
    calculadora=input('Você deseja entrar! Digite 1 para o acesso:')

    if calculadora=='1':
        n1=float(input('Digite um valor:'))
        n2=float(input('Digite outro valor:'))
        print(f'O valor é {n1+n2:.1f}')
else:
    print('Você saiu')
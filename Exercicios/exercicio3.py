Nome = None

entrada = input('Digite seu nome: ') #define a entrada do usuário
if entrada == '':
    print('O nome não foi definido') #define se o usuário escreveu ou não o nome
    exit() #encerra o programa caso o usuário não digite nada

else:
    Nome = entrada
    print(f'Seu nome é {Nome}')

acesso=input(f'Olá, {entrada}! Seja bem vindo, você deseja entrar ou sair?') #define se o usuário deseja entrar ou sair
senha_permitida= '1921' #define a senha permitida para o acesso, caso o usuário queira entrar
senha=input('Por favor, digite a senha:')

if (acesso == 'Entrar' or acesso == 'entrar') and senha==senha_permitida:
    calculadora=input('Você deseja entrar! Digite 1 para o acesso:')

    if calculadora=='1': #calculadora simples, onde o usuário digita dois números e o programa retorna a soma dos dois
        n1=float(input('Digite um valor:'))
        n2=float(input('Digite outro valor:'))
        print(f'O valor é {n1+n2:.1f}')
else: #saída do programa caso o usuário digite 'sair' ou a senha esteja incorreta
    print('Você saiu')
usuarios = ["ana", "carlos", "beatriz"]
usuario = "carlos"
senha = "1234"
senha_correta = "1234"

if usuario in usuarios:
    if senha == senha_correta:
        print("Acesso liberado!")
    else:
        print("Senha incorreta!")
else:
    print("Usuário não autorizado!")
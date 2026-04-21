alunos = [         
    ['Ana', 8],
    ['Carlos', 4],
   ['Beatriz', 6],
   ['Pedro', 9],
    ['Julia', 3],
]

aprovados = 0 
for aluno in alunos: 
    nome = aluno[0]
    nota = aluno[1]

    if nota >= 7:
        print(f'{nome}: Aprovado!')
        aprovados = aprovados + 1
        if nota >= 5 and nota < 7:
            print(f'{nome}: Recuperação!')
    else:
        print(f'{nome}: Reprovado!')

print(f'Total de aprovados: {aprovados}')
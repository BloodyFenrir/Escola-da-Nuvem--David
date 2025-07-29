# Registro de notas e cálculo da média da turma

quantidade_alunos = int(input("Quantos alunos na turma? "))
soma_notas = 0

for i in range(1, quantidade_alunos + 1):
    nota = float(input(f"Digite a nota do aluno {i}: "))
    soma_notas += nota

media = soma_notas / quantidade_alunos

print("Média da turma:", round(media, 2))# Registro de notas e cálculo da média da turma

quantidade_alunos = int(input("Quantos alunos na turma? "))
soma_notas = 0

for i in range(1, quantidade_alunos + 1):
    nota = float(input(f"Digite a nota do aluno {i}: "))
    soma_notas += nota

media = soma_notas / quantidade_alunos

print("Média da turma:", round(media, 2))
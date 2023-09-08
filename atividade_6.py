#ATIVIDADE 6

alunos = {}

for i in range(3):
    nome = input(f"Digite o nome do {i+1}º aluno: ")
    nota = float(input(f"Digite a nota do {i+1}º aluno: "))
    alunos[nome] = nota

soma_notas = 0
for nota in alunos.values():
    soma_notas += nota

media = soma_notas / len(alunos)

print("\nDados dos alunos:")
for nome, nota in alunos.items():
    print(f"Aluno: {nome}, Nota: {nota}")
    
print(f"Média das notas: {round(media, 2)}")
# Inicializamos a variável com um valor bem baixo
maior_nota = -1.0

print("Digite as 5 notas dos alunos:")

for i in range(5):
    nota = float(input(f"Digite a nota do {i + 1}º aluno: "))
    
    # Se a nota atual for maior que a maior_nota registrada, ela assume o trono
    if nota > maior_nota:
        maior_nota = nota

print("-" * 25)
print(f"A maior nota do grupo foi: {maior_nota}")
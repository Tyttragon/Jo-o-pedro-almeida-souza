# Solicita a quantidade de alunos
total_alunos = int(input("Digite a quantidade de alunos: "))

# Inicializa os contadores
aprovados = 0
recuperacao = 0
reprovados = 0

# Loop para ler a média de cada aluno
for i in range(total_alunos):
    media = float(input(f"Digite a média do aluno {i + 1}: "))
    
    # Lógica de classificação
    if media >= 7:
        aprovados += 1
    elif 4 <= media < 7:
        recuperacao += 1
    else:
        reprovados += 1

# Exibe o relatório final
print("\n--- Resultado Final ---")
print(f"Aprovados:   {aprovados}")
print(f"Recuperação: {recuperacao}")
print(f"Reprovados:  {reprovados}")
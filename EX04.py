idade = int(input("Digite sua idade: "))
experiencia = int(input("Digite seus anos de experiência: "))

# Aplica a Regra Lógica: Acesso=(Idade≥18) AND (Experiencia>2)
acesso_liberado = (idade >= 18) and (experiencia > 2)

# Saída conforme o formato esperado
print(f"Acesso Liberado: {acesso_liberado}")
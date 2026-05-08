# Inicializa a variável para o total acumulado (opcional, mas útil)
total_geral = 0
contador_compras = 0

while True:
    # Solicita o valor da compra
    valor = float(input("Digite o valor da compra: R$ "))
    
    # Atualiza os totais
    total_geral += valor
    contador_compras += 1
    
    # Pergunta se o usuário deseja continuar
    continuar = input("Deseja continuar? (S/N): ").strip().upper()
    
    # Verifica a condição de parada
    if continuar == 'N':
        break
    elif continuar != 'S':
        print("Opção inválida, mas assumirei que deseja parar.")
        break

# Exibe o resumo ao encerrar
print("\n--- Resumo das Compras ---")
print(f"Quantidade de itens: {contador_compras}")
print(f"Valor total: R$ {total_geral:.2f}")
print("Programa encerrado. Volte sempre!")
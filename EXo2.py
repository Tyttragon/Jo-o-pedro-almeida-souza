# solicitando os dados
valor_hora = float(input("digite o valor cobrado por hora (RS$)= "))
horas_estimadas = float(input("digite a estimativa de horas para a conclusão"))

# cálculos baseados nas fórmulas fornecidas
valor_bruto = horas_estimadas * valor_hora
impostos =  valor_bruto * 0.15
valor_liquido = valor_bruto - impostos

# exibindo os resultados
print("-" * 30)
print(f"RESUMO DO PROJETO")
print("-" * 30)
print(f"Valor Bruto: R${valor_bruto:,.2f}")
print(f"impostos (15%): R${impostos:,.2f}")
print(f"valor Líquido: R${valor_liquido:,.2f}")
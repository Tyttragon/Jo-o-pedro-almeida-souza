salario = float(input("Digite o salário atual: "))

if salario <= 1500:
    aumento = 0.15
elif salario <= 3000:
    aumento = 0.10
else:
    aumento = 0.05

novo_salario = salario * (1 + aumento)
print(f"Novo salário: R$ {novo_salario:.2f}")
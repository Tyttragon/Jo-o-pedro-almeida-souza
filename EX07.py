soma = 0

for i in range(8):
    valor = int(input(f"Digite o {i+1}º valor inteiro: "))
    if valor % 2 == 0:
        soma += valor

print(f"A soma dos números pares é: {soma}")
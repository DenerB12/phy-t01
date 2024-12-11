compras = int(input("Quantas compras foram realizadas: "))

numero = 0
quantidade = 0

while compras > numero:
    numero += 1
    valor = float(input("Digite o valor da compra: "))
    quantidade = quantidade + valor

print(f"Você gastou um total de R$ {quantidade}")


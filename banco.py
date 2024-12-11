dinheiro = 500
s = False

print(f'Seu saldo atual: R${dinheiro}')

while not s == True:
    pergunta = input("1) Depositar - 2) Sacar - S) sair\n")
    if pergunta == "1":
        depositar = int(input("Digite o valor a ser depositado: "))
        dinheiro = dinheiro + depositar
        continue
    elif pergunta == "2":
        sacar = int(input("Digite o valor a ser sacado: "))
        dinheiro = dinheiro - sacar
    elif pergunta == "s":
        s = True
    else:
        print("Por favor, Escolha uma das opções abaixo para prosseguir:\n")
        continue

print(f"Saldo final: R${dinheiro}")

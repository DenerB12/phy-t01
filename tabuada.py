tabuada = int(input("Digite um número para saber sua tabuada: "))

n1 = 0
n10 = 10

while n10 >= n1:
    resultado = tabuada * n1
    print(f"{tabuada} x {n1} = {resultado}")
    n1 += 1
# dia = int(input("informe o dia da semana de 1 a 7: "))

# match dia:
#     case 1: print("Domingo")
#     case 2: print("Segunda-feira")
#     case 3: print("Terça-feira")
#     case 4: print("Quarta-feira")
#     case 5: print("Quinta-feira")
#     case 6: print("Sexta-feira")
#     case 7: print("Sábado")
#     case _: print("Dia inválido")

# farol = "Verde"

# match farol:
#     case "Verde": print("Pode ir")
#     case "Amarelo": print("Reduza")
#     case "Vermelho": print("Pare!")
#     case _: print("Cada um por si!")


# Loop

# for cada_elemento in algum_iteravel:
#     bloco_indentado

# texto = "Por exemplo"
#
# conta_letras = 0
#
# for letra in texto:
#     # print(letra, end="---")
#     conta_letras = conta_letras + 1

# numero_repeticao = int(input("Informe o número de repetições: "))
#
# for i in range(numero_repeticao):
#     if i % 2 == 0: print(i, "par")
#
#     else: print(i, "impar")

# # for i in range(5, 40, 2):
#     print(i)

# numero = int(input("Informe o número que se deve apresentar a tabuada: "))
#
# print(f"Vamos ver a tabuada do {numero}:")
#
# for num in range(1, 11, 1):
#     print(num * numero)

# import time

# for i in range(10, -1, -1):
#
#     print("\r", end=str(i))
#     time.sleep(0.1)

# tempo = 3600
#
# for i in range(tempo, -1, -1):
#     print("\r", end=f"{i//3600}:{i//60}:{i%60}")
#     time.sleep(1)

i = 0

while i < 10:
    i += 1
    print(i)
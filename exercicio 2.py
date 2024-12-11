# lado1 = int(input("Informe o lado A: "))
# lado2 = int(input("Informe o lado B: "))
# lado3 = int(input("Informe o lado C: "))
#
# if lado1 + lado2 > lado3:
#     if lado1 == lado2 == lado3:
#         print("Isso é um Triângulo Equilátero!")
#     elif lado1 != lado2 != lado3:
#         print("Isso é um Triângulo Escaleno")
#     else:
#         print("Isso é um Triângulo Isóscele5s")
#

# Receber os lados do triângulo

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

# Verificar se os lados informados formam um triângulo

# a + b > c
# b + c > a
# c + a > b

print()

if a + b > c and b + c > a and  c + a > b:
    print(f'{a}, {b} e {c} formam um triângulo do tipo: ', end='')
    # Equilátero
    if a == b == c: print("Equilátero.")

    # Isóceles
    elif a == b or b == c or c == a: print("Isóceles.")

    # Escaleno
    elif a != b != c: print("Escaleno.")

else:
    print(f'{a}, {b} e {c} não formam um triângulo.')

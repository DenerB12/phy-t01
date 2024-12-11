# condicao_1 = 10 > 100  # False
# print(condicao_1)
#
# condicao_2 = 2 == 2  # True
# print(condicao_2)
#
# print(condicao_1 and condicao_2)
from traceback import print_tb

# authentic_user = True
# authentic_password = True
#
# libera_user = authentic_user + authentic_password
#
# print(libera_user)


# dinheiro = False
# cartao = True
#
# pagamento = dinheiro or cartao
#
# print(pagamento)

# print (not False)
# print (not True)

# caixa_cheia = False
#
# encher_caixa = not caixa_cheia
#
# print(encher_caixa)

# print(not 10 > 5 and 20 % 2 == 0 or 8 >= 4)

# codigo_produto = input("Informe o código do produto: ").upper()
#
# quantidade_minima = 1000
# quantidade_maxima = 2500
#
# # Contexto 1 de decisão
# if codigo_produto == "LED20":
#     quantidade_estoque = int(input(f"Informe a quantidade de {codigo_produto} em estoque: "))
#     if quantidade_estoque < quantidade_minima:
#         unidades_compra = quantidade_minima - quantidade_estoque
#         print(f"Compre {quantidade_minima - quantidade_estoque} unidades do produto {codigo_produto}.")
#
#     elif quantidade_estoque > quantidade_maxima:
#         unidades_venda = quantidade_estoque - quantidade_maxima
#         print(f"Venda {unidades_venda} unidades de {codigo_produto}")
#
#     else:
#         print(f"Não há necessidade de comprar mais unidades de {codigo_produto}")
# else:
#     print(f"{codigo_produto} não existe no nosso sistema.")

# Lição 1
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))

media = (nota1 + nota2) / 2
print(f"A média do aluno foi {media}")

if media == 10:
    print("Aprovado com Distinção!")

elif media >= 7:
    print("Aprovado!")

else:
    print("Reprovado!")
    
# Lição 2

# lado1 = float(input("Informe o primeiro lado: "))
# lado2 = float(input("Informe o segundo lado: "))
# lado3 = float(input("Informe o terceiro lado: "))
#
# if lado1 + lado2 > lado3:
#     if lado1 == lado2 == lado3:
#         print("Isso é um Triângulo Equilátero!")
#     elif lado1 != lado2 != lado3:
#         print("Isso é um Triângulo Escaleno")
#     else:
#         print("Isso é um Triângulo Isósceles")

# Lição 3

salario = int(input("Digite o salário: "))

if salario >= 2000:
    desconto = salario * 0.1
    salario_li = salario - desconto
    print(f"Salário Líquido: {salario_li:.2f}")

elif salario >= 3500:
    desconto = salario * 0.15
    salario_li = salario - desconto
    print(f"Salário Líquido: {salario_li:.2f}")

elif salario >= 5000:
    desconto = salario * 0.2
    salario_li = salario - desconto
    print(f"Salário Líquido: {salario_li:.2f}")
else:
  print("Isento")



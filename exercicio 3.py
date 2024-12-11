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

from aula_6 import teste


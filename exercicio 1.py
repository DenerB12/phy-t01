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
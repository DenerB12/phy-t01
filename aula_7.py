
# i = 0
#
# while i < 10:
#     print(i)
#     i += 1

# somador = 0
#
# while somador < 100:
#     somador += int(input("Digite um número a ser somado: "))
#     print(somador)

# import time
#
# tempo = 3600
#
# while tempo > -1:
#     print("\r", end=f"{tempo//3600}:{tempo//60}:{tempo%60}")
#     time.sleep(1)
#     tempo -=1

# while True:
#
#     email = input("E-mail: ")
#
#     if email[-4:] != ".com":
#         print("Falta o .com")
#         continue
#
#
#     else:
#         print("Bem-vindo")
#         break

# acesso = "Dener.12"
# controle_acesso = False
# chance = 3
#
# while not controle_acesso:
#     chave_acesso = input("Informe sua credencial: ")
#
#     if chance > 0:
#
#         if chave_acesso == acesso:
#
#             controle_acesso = True
#             print("\nBem-vindo ao sistema.")
#
#         else:
#             chance -= 1
#             continue
#     else:
#         print("Acesso Bloqueado")
#         break

palavra = input("Entre com a palavra: ").lower()
jogo = ["_" for letra in palavra]  # Cria uma lista com "_" para cada letra da palavra

print("Vamos Jogar Forca!")
print("\nPalavra Secreta:", " ".join(jogo))

chances = 6
letras_usadas = set()

while chances > 0:
    letra = input("Fale uma letra: ").lower()

    if letra in letras_usadas:
        print("Você já usou essa letra!")
    else:
        letras_usadas.add(letra)

        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    jogo[i] = letra
            print("".join(jogo))
        else:
            chances -= 1
            print(f"Essa letra não tem, sobraram {chances} chances.")

    if "_" not in jogo:  # Verifica se todas as letras foram descobertas
        print("Você acertou!")
        break

if "_" in jogo:
    print("Que pena, você perdeu!")
    print("A palavra era:", palavra)
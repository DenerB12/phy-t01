contatos = {
    "Dener": '91236-8002',
    "Paulo": '96875-4552',
    "João": '95663-0132',
        }

# Add a lista
contatos["José"] = "98540-7845"
print(contatos)

# Removendo contato
del contatos["José"]
print(contatos)

# Modificando numero
contatos["Dener"] = "91232-8112"
print(contatos)

# Imprimindo todos os nomes
for nome in contatos:
    print(nome)


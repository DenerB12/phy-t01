produtos = {
    "Bananas": {'Preço': 10.0, 'Quantidade': 20},
    "Maçãs": {'Preço': 5.0, 'Quantidade': 15},
    "Morango": {'Preço': 12.0, 'Quantidade': 10}
}

while True:

    print(produtos)

    print("""
    1 - Adicionar produto
    2 - Consultar informação
    3 - Alterar o preço
    4 - Remover um produto
    """)
    opcao = input("Escolha uma das opções acima: ").strip()

    if opcao == "1":
        nome = input('Qual o nome do produto?: ')
        valor = float(input('Qual o valor do produto?: '))
        quantidade = int(input('Qual a quantidade deste produto?'))
        produtos[nome] = {"Preço": valor, "Quantidade": quantidade}
        print(f'\n-----{nome} adicionado na lista-----\n')

    elif opcao == "2":
        consulta = input('Digite o nome do produto: ')
        if consulta in produtos:
            print(f'\n------informações do produto {consulta}------\n')
            print(f"Preço: R${produtos[consulta]['Preço']:.2f}")
            print(f'Quantidade em estoque: {produtos[consulta]["Quantidade"]}\n')
        else:
            print('Produto não encontrado')

    elif opcao == "3":
        novo = input('Qual produto você deseja alterar o valor: ')
        if novo in produtos:
            novo_valor = float(input(f'Digite o novo valor para o produto {novo}: '))
            produtos[novo]['Preço'] = novo_valor
            print(f'Preço do produto {novo} alterado prar R$ {novo_valor:.2f}.')

    elif opcao == "4":
        deletar = input('Digite o nome do item que deseja deletar: ')
        if deletar in produtos:
            del produtos[deletar]
            print(f'\n-----{deletar} deletado da lista-----\n')
            continue

    else:
        print('Escolha uma das opções abaixo para continuar!\n')




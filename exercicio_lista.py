lista_frutas = ['banana','maçã','melancia','morango','uva']

# Primeira e ultima
print(lista_frutas[0], lista_frutas[-1])

# Adicionar 3 frutas
lista_frutas.append('pera')
lista_frutas.append('abacate')
lista_frutas.append('mamão')

print(lista_frutas)

# Remover o segundo item da lista
del lista_frutas[1]

print(lista_frutas)

# Ordem alfabetica
lista_frutas.sort()

# Contar quantas bananas tem na lista
quantidade = lista_frutas.count('banana')
print(f'banana aparece {quantidade} vezes')
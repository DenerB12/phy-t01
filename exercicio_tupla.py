tupla_dados = ('Dener','17','SBC')
hobbies = ('Esporte','Musica','Jogar')

# Printando um abaixo do outro
esporte, musica, jogar = hobbies
nome, idade, cidade = tupla_dados
print(nome)
print(idade)
print(cidade)

# Tentar modificar o pimeiro item
#tupla_dados[0] = 'Paulo' # Não é possível pois a tupla é imutavel

# Nova tupla Hobbies
tudo = tupla_dados + hobbies
print(tudo)
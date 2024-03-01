# %%
notas = []
nota = 7.75

notas.append(nota)
print(notas)

notas.append(10)
print(notas)

notas.append([5.75, 6.24]) # adiciona um elemento (a lista [5.75, 6.24]) dentro da lista notas
print(notas)
len(notas) # núm. de elementos dentro da lista

notas.extend([5.75, 6.24]) # adiciona uma lista dentro da lista notas
print(notas)
len(notas)

notas = notas + [10, 9.25] # concatenar
print(notas)

# %%

notas.remove(10)
print(notas)

# %%
nome = 'milena'
nome_alto = nome.upper()
print(nome_alto)
print(nome)

# %%

nomes = ['teo', 'milena', 'eduardo']
for i in nomes:  # aqui o i é uma string porque os dados da lista são strings
    print(i.title())
    
nomes.extend(['jose', 'lila'])
print(nomes)

nomes.extend('greta') # adiciona cada letra como uma string
print(nomes)

# adicionar 1 elemento: append
# adicionar vários: extend

# %%

dados = ['Teo', 'Calvo', 31, ['Milena', 'Eduardo', 'Greta'], ['Jade']]

# acessando Milena:
dados[3][0]

# acessando Greta:
dados[3][-1]

# acessando Eduardo:
dados[3][-2]
lindo = dados[3][-2]
print(lindo)

# Primeira letra do nome Jade
dados[-1][0][0]


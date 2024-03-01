# %%

# "idade:""40"  chave:valor
dados = {"nome":"Milena",
         "sobrenome":"Villar",
         "idade":40,
         "conjuge":"Eduardo",
         "pais":["Vivianne Fulber", "Ricardo Villar"],
         "irmas": [{"nome":"Jade", "idade":26}, {"nome":"Carol", "idade":25}, {"nome":"Ba", "idade":27}]}

nome = dados["nome"]
print(nome)

# Idade da Jade
print(dados["irmas"][0]["idade"])

# %%
# valores do dicionario
dados.values()
print(list(valores))

# %%
dados.keys()

# %
dados.items()

# 1. Faça um programa que vende uma garrafa de água:
# a. Se o cliente escolher água mineral natural, será cobrado R$1,50
# b. Se o cliente escolher água mineral com gás, será cobrado R$2,50


escolha = input("Você gostaria de uma garrafa de água natural ou gás? [natural]/[gas]: ")

if escolha == "natural":
    print("Você me deve R$ 1,50")
    
elif escolha == "gas":
    print("Você me deve R$ 2,50")
    
else:
    print("Faça uma escolha válida!")
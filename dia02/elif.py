# %%
idade = int(input("Entre com a sua idade: "))

if idade < 18:
    print("Você é menor de idade!")
    
elif idade > 90:
    print("Cuidado, você já tem certa idade!")
    
else:
    print("Beba a vontade! Você é maior de idade!")
    
# %%

if 18 <= idade <= 89:
    print("Beba a vontade! Você é maior de idade!")
    
elif idade >= 90:
    print("Cuidado, você já tem certa idade!")
    
else:
    print("Você é uma criança! Vá para casa!")

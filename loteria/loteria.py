
numero_sorte = 7

for i in range(3):  # 3 tentativas
    
    while True: 
        try:
            numero = int(input("Entre com um número entre 1 e 15: "))
            break
            
        except ValueError:
            #continue   #Usar se não tiver o while; ignora o que está abaixo e volta para "Entre com um número entre 1 e 15:
            print("Digite um número!!!!!")
            
    if numero == numero_sorte:
        print("Você acertou!")
        break
    
    elif numero > numero_sorte:
        print("Você errou! Tente um número menor!")
    else:
        print("Você errou! Tente um número maior!")
        


# contornando o erro caso a resposta não seja em formato inteiro
   # try:
    #    numero = int(input("Entre com um númrero entre: "))
        
    #except ValueError as err:
        # print(err) # caso queira mostrar o erro
    #    print("Digite um número!!!!")

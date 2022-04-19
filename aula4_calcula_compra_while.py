prod = input("Deseja começar a calcular o valor da sua compra? ")
total = 0
indice = 1

while prod == "s" or prod == "sim":
    preco = float(input(f"Digite o valor do {indice}° produto: "))
    indice += 1
    total += preco 
    prod = input("Tem mais produtos? (Digite -1 se não tiver mais produtos) ")
    if prod == -1:
        break
    
if total != 0:
    print(f"O valor da compra foi de R${total}!")
else:
    print(f"Programa Encerrado!")

# Sistema de desconto de veiculos
# solicitar o nome do veiculo e preco 
# se o preco for maio  que 80k terá 60% de desconto
# # se for maior que 50k terá 30%
# se for menor que 30 não tem desconto

print("Digite o nome do veiculo")
nomeCarro = input()

print("Digite o preço do veiculo")
precoCarro = float(input())

if precoCarro >= 80000:
    desconto = precoCarro * 60 / 100
    precoFinal = precoCarro - desconto
    print("O preço do carro tem 60 de desconto e seu preço será")
    print(precoFinal)
elif precoCarro > 50000 and precoCarro < 80000:
    desconto = precoCarro * 30 / 100
    precoFinal = precoCarro - desconto
    print("O preço do carro tem 30 de desconto e seu preço será ")
    print(precoFinal)
else:
    print("Seu carro não tem desconto.")
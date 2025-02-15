#Saber se é uma palavra é um palindromo ou nao

print("Digite a palavra que deseja saber se é palíndromo ou não.")
palavra = input().lower().strip().replace('','')

if palavra == palavra[::-1]:
    print("É palíndromo")
else:
    print("Não é palíndromo")
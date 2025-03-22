import csv

with open("dados.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Nome, Idade, Cidade\n")
    arquivo.write("Yuri Alberto, 23, São Bernardo Campo\n")
    arquivo.write("Arthur, 94, Cotia\n")
    arquivo.write("Rafael, 18, Taboão da Serra\n")

with open("dados.txt", "r", encoding="utf-8") as arquivo:
    print("Conteúdo do arquivo txt:")
    print(arquivo.read())

#CRIAR ARQUIVO CSV
dados = [
    ["Nome","Idade","Cidade"],
    ["Felipe","20","JD MONTE ALEGRE"],
    ["Ana Bea","17","Sandra"]
]

with open("dados.csv", "w", newline="", encoding="utf-8") as csvarquivo:
    escritor = csv.writer(csvarquivo)
    escritor.writerows(dados)

with open("dados.csv", "r", encoding="utf-8") as csvarquivo:
    leitor = csv.reader(csvarquivo)
    print("\nConteúdo do arquivoo CSV")
    for linha in leitor:
        print(linha)
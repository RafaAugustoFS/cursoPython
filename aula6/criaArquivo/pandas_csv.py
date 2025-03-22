import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "Nome": ["Arthur", "Maria", "Mafius", "ROger", "Alou"],
    "Idade": [32, 17, 42, 19,18],
    "Cidade": ["Granja", "Vila Iase","Morro do Macaco", "Vista Alegre", "Morro Grande"]
}

df = pd.DataFrame(dados)
print(df)

#Visualizar em dataframe o csv
df_csv = pd.read_csv("pandas_dados.csv")

df_filtrado = df[df["Idade"] > 25]
print(df_filtrado)

# //Decrescete
df_ordenado = df.sort_values(by="Idade", ascending=False)
print(df_ordenado)

# Exibir estatisticas
print(df.describe())

media_cidade = df.groupby("Cidade")["Idade"].mean()
print(media_cidade)

# df.plot(kind="line", x="Nome", y="Idade", color="blue")
# plt.title("Idade das pessoas")
# plt.xlabel("Nome")
# plt.ylabel("Idade")
# plt.show()

df.boxplot(column="Idade", by="Cidade", grid=False)
plt.title("Distribuição de idades por cidade")
plt.xlabel("Cidade")
plt.ylabel("Idade")

plt.show()
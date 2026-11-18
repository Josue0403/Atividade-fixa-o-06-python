##Gráfico de barras agrupadas: vendas médias por categoria e região.
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados/barras.csv")
tabela = df.pivot(index="categoria", columns="regiao", values="vendas_medias")
tabela = tabela.loc[df["categoria"].unique(), ["Norte", "Sul", "Leste", "Oeste"]]

ax = tabela.plot(kind="bar", figsize=(10, 6), width=0.8, edgecolor="white")
ax.set_title("Vendas médias por categoria e região")
ax.set_xlabel("Categoria")
ax.set_ylabel("Vendas médias")
ax.set_xticklabels(tabela.index, rotation=0)
ax.legend(title="Região")
ax.grid(axis="y", alpha=0.3)
ax.set_axisbelow(True)
plt.tight_layout()
plt.savefig("grafico_barras.png", dpi=150)
plt.show()
##Gráfico de distribuição: histograma das idades dos clientes.
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados/distribuicao.csv")

fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(df["idade"], bins=15, color="#55a868", edgecolor="white")
ax.axvline(df["idade"].mean(), color="red", linestyle="--",
           label=f"Média: {df['idade'].mean():.1f}")
ax.axvline(df["idade"].median(), color="black", linestyle=":",
           label=f"Mediana: {df['idade'].median():.1f}")

ax.set_title("Distribuição da idade dos clientes")
ax.set_xlabel("Idade (anos)")
ax.set_ylabel("Número de clientes")
ax.legend()
ax.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig("grafico_distribuicao.png", dpi=150)
plt.show()
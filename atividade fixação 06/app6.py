##Gráfico de pizza: participação de cada canal no faturamento.
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados/pizza.csv").sort_values("faturamento", ascending=False)

fig, ax = plt.subplots(figsize=(7, 7))
ax.pie(df["faturamento"], labels=df["canal_venda"], autopct="%1.1f%%",
       startangle=90, counterclock=False,
       wedgeprops={"edgecolor": "white", "linewidth": 2})
ax.set_title("Participação dos canais de venda no faturamento")
plt.tight_layout()
plt.savefig("grafico_pizza.png", dpi=150)
plt.show()
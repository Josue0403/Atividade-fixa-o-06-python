##Gráfico de linhas: evolução diária das vendas (jan–mar/2026).
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados/linhas.csv", parse_dates=["data"]).sort_values("data")
df["media_movel_7d"] = df["vendas"].rolling(7).mean()

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df["data"], df["vendas"], color="#4c72b0", alpha=0.6, label="Vendas diárias")
ax.plot(df["data"], df["media_movel_7d"], color="#c44e52", linewidth=2.5,
        label="Média móvel (7 dias)")

ax.set_title("Evolução das vendas diárias — 1º trimestre de 2026")
ax.set_xlabel("Data")
ax.set_ylabel("Vendas")
ax.grid(alpha=0.3)
ax.legend()
fig.autofmt_xdate()
plt.tight_layout()
plt.savefig("grafico_linhas.png", dpi=150)
plt.show()
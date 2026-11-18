##Heatmap: movimento de clientes por dia da semana e horário.
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados/heatmap.csv")

ordem_dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
tabela = df.pivot(index="dia_semana", columns="horario", values="movimento_clientes")
tabela = tabela.reindex(ordem_dias)

fig, ax = plt.subplots(figsize=(9, 5.5))
im = ax.imshow(tabela.values, cmap="YlOrRd", aspect="auto")

ax.set_xticks(range(len(tabela.columns)), tabela.columns)
ax.set_yticks(range(len(tabela.index)), tabela.index)
for i in range(tabela.shape[0]):
    for j in range(tabela.shape[1]):
        v = tabela.iloc[i, j]
        ax.text(j, i, int(v), ha="center", va="center",
                color="white" if v > tabela.values.max() * 0.6 else "black")

ax.set_title("Movimento de clientes por dia e horário")
ax.set_xlabel("Horário")
ax.set_ylabel("Dia da semana")
fig.colorbar(im, ax=ax, label="Clientes")
plt.tight_layout()
plt.savefig("grafico_heatmap.png", dpi=150)
plt.show()
##Gráfico de frequência: quantidade de chamados por tipo de atendimento.
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados/frequencia.csv")
freq = df["tipo_atendimento"].value_counts()

fig, ax = plt.subplots(figsize=(8, 5))
barras = ax.bar(freq.index, freq.values, color="#4c72b0")
ax.bar_label(barras, padding=3)

ax.set_title("Frequência de chamados por tipo de atendimento")
ax.set_xlabel("Tipo de atendimento")
ax.set_ylabel("Número de chamados")
ax.grid(axis="y", alpha=0.3)
ax.set_axisbelow(True)
plt.tight_layout()
plt.savefig("grafico_frequencia.png", dpi=150)
plt.show()

##Boxplot: distribuição de salários por departamento (com outliers).
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados/boxplot.csv")
ordem = df["departamento"].unique()
dados = [df.loc[df["departamento"] == d, "salario"] for d in ordem]

fig, ax = plt.subplots(figsize=(9, 6))
ax.boxplot(dados, tick_labels=ordem, patch_artist=True,
           boxprops={"facecolor": "#a6cee3"},
           medianprops={"color": "black", "linewidth": 2},
           flierprops={"marker": "o", "markerfacecolor": "#c44e52",
                       "markeredgecolor": "#c44e52"})

ax.set_title("Distribuição de salários por departamento")
ax.set_xlabel("Departamento")
ax.set_ylabel("Salário (R$)")
ax.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig("grafico_boxplot.png", dpi=150)
plt.show()
##Gráfico de dispersão: altura x peso, colorido por sexo.
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados/dispersao.csv")

fig, ax = plt.subplots(figsize=(8, 6))
cores = {"Masculino": "#1f77b4", "Feminino": "#e377c2"}
for sexo, grupo in df.groupby("sexo"):
    ax.scatter(grupo["altura_cm"], grupo["peso_kg"], label=sexo,
               color=cores[sexo], alpha=0.7, edgecolor="white", s=50)

ax.set_title("Relação entre altura e peso")
ax.set_xlabel("Altura (cm)")
ax.set_ylabel("Peso (kg)")
ax.grid(alpha=0.3)
ax.legend(title="Sexo")
plt.tight_layout()
plt.savefig("grafico_dispersao.png", dpi=150)
plt.show()
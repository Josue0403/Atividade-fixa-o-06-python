##Regressão linear: renda mensal x gasto mensal.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados/regressao.csv")
x, y = df["renda_mensal"], df["gasto_mensal"]

a, b = np.polyfit(x, y, 1)           # y = a*x + b
r2 = np.corrcoef(x, y)[0, 1] ** 2
xs = np.linspace(x.min(), x.max(), 100)

fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(x, y, alpha=0.7, color="#4c72b0", edgecolor="white", label="Observações")
ax.plot(xs, a * xs + b, color="#c44e52", linewidth=2.5,
        label=f"Regressão: y = {a:.2f}x + {b:.0f}  (R² = {r2:.3f})")

ax.set_title("Regressão linear: renda x gasto mensal")
ax.set_xlabel("Renda mensal (R$)")
ax.set_ylabel("Gasto mensal (R$)")
ax.grid(alpha=0.3)
ax.legend()
plt.tight_layout()
plt.savefig("grafico_regressao.png", dpi=150)
plt.show()
import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

dados = pd.read_excel(
    "calc1reg.xlsx",
    sheet_name="Planilha1",
    header = 1,
    usecols= "B:H"
)

dados = dados.dropna(subset=[dados.columns[0]])

x = dados.iloc[:,0].astype(float)
rodadas = dados.iloc[:, [2,3,4]].astype(float)
y = rodadas.mean(axis=1)

#regressão linear
resultado = linregress(x,y)

a = resultado.intercept
b = resultado.slope
r2 = resultado.rvalue **2

x_reta = np.linspace(x.min(), x.max(), 100)
y_reta = a+b*x_reta

#construção do grafico
plt.scatter(x,y,label="Medias observadas")
plt.plot(
     x_reta,y_reta,color="red",label="Regressão linear"
)

plt.xlabel("quantidade de aplicativos abertos")
plt.ylabel("RAM utilizada(GB)")
plt.title("quantidade de aplicativos x uso de RAM")
plt.legend()
plt.grid(True)

plt.savefig("grafico_regressao.png", dpi=300)
plt.show()

print(f"Intercepto (a): {a:.4f}")
print(f"Inclinacao (b): {b:.4f} GB por aplicativo")
print(f"Coeficiente de determinacao (R²): {r2:.4f}")
print(f"Equacao: y = {a:.4f} + {b:.4f}x")
import matplotlib.pyplot as plt
import numpy as np

# Datos
intentos = [1, 2, 3, 4, 5]
longitudes = [75.2, 75.25, 75.2, 75.2, 75.25]

# Promedio
promedio = np.mean(longitudes)

plt.figure()

# Puntos azules
plt.scatter(intentos, longitudes, 
            color='royalblue', label="Mediciones")

# Línea del promedio (solo línea, sin puntos)
plt.axhline(promedio, linestyle='--',
            color='crimson',
            label=rf"Promedio = {promedio:.2f} $\times 10^{{-3}}$ m")

plt.xlabel("Intento")
plt.ylabel(r"Longitud ($\times 10^{-3}$ m)")
plt.title("Mediciones de longitud del cilindro")

plt.grid(alpha=0.3)
plt.legend()

plt.savefig("grafico_dispersion_longitud.png")
# plt.show()
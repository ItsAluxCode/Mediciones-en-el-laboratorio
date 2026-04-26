import matplotlib.pyplot as plt
import numpy as np

# Datos (diámetro en mm ≡ x10^-3 m)
intentos = [1, 2, 3, 4, 5]
diametros = [21.45, 21.50, 21.40, 21.45, 21.40]

# Promedio
promedio = np.mean(diametros)

plt.figure()

# Puntos (azul)
plt.scatter(intentos, diametros,
            color='royalblue', label="Mediciones")

# Línea del promedio (rojo)
plt.axhline(promedio, linestyle='--',
            color='crimson',
            label=rf"Promedio = {promedio:.2f} $\times 10^{{-3}}$ m")

# Etiquetas
plt.xlabel("Intento")
plt.ylabel(r"Diámetro ($\times 10^{-3}$ m)")
plt.title("Mediciones del diámetro del cilindro")

# Estética
plt.grid(alpha=0.3)
plt.legend()

# Guardar
plt.savefig("grafico_dispersion_diametro.png")
# plt.show()
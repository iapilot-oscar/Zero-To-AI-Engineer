import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# -----------------------------------------------------------
# CONFIGURACIÓN: Carga y Definición de la Matriz de ESCALA DE GRISES
# -----------------------------------------------------------

# 1. CARGAR DATOS REALES
print("1. Cargando imagen original...")
img = np.array(Image.open("foto.jpg"))

# 2. SEPARAR CANALES (Slicing)
r = img[:,:,0] 
g = img[:,:,1] 
b = img[:,:,2] 

# 3. TRANSFORMACIÓN MATEMÁTICA (Fórmula de PROMEDIO para Grises)
print("2. Calculando 70 millones de operaciones para el filtro escala de grises...")
# Convertimos a 'int' o 'float' ANTES de sumar para evitar que se desborde el límite de 255
new_gris = (r.astype(float) + g.astype(float) + b.astype(float)) / 3

# 4. RECONSTRUIR Y SANITIZAR
img_gris = np.stack([new_gris, new_gris, new_gris], axis=2)
# Aseguramos que los valores sean enteros y no superen 255.
img_gris = np.clip(img_gris, 0, 255).astype('uint8')


# -----------------------------------------------------------
# EXPORTACIÓN: Guardar la Matriz como Archivo
# -----------------------------------------------------------

# Convertimos la matriz NumPy de vuelta a un objeto de Imagen PIL
img_gris_pil = Image.fromarray(img_gris)

# Usamos la función .save() para escribir el archivo en el disco.
NOMBRE_ARCHIVO_SALIDA = "foto_gris_output2.png"
img_gris_pil.save(NOMBRE_ARCHIVO_SALIDA)

print(f"3. ✅ ¡Transformación completa y guardada como: {NOMBRE_ARCHIVO_SALIDA}")

# 5. VISUALIZACIÓN (Opcional, pero útil)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1); plt.imshow(img); plt.title("Original")
plt.subplot(1, 2, 2); plt.imshow(img_gris); plt.title("Gris Generada")
plt.show()
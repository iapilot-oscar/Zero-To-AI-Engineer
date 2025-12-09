import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# -----------------------------------------------------------
# CONFIGURACIÓN: Carga y Definición de la Matriz Sepia
# -----------------------------------------------------------

# 1. CARGAR DATOS REALES
print("1. Cargando imagen original...")
img = np.array(Image.open("foto.jpg"))

# 2. SEPARAR CANALES (Slicing)
r = img[:,:,0] 
g = img[:,:,1] 
b = img[:,:,2] 

# 3. TRANSFORMACIÓN MATEMÁTICA (Fórmula Sepia)
print("2. Calculando 70 millones de operaciones para el filtro Sepia...")
# Calculamos las nuevas intensidades (el valor de cada canal)
new_r = (r * 0.393) + (g * 0.769) + (b * 0.189)
new_g = (r * 0.349) + (g * 0.686) + (b * 0.168)
new_b = (r * 0.272) + (g * 0.534) + (b * 0.131)

# 4. RECONSTRUIR Y SANITIZAR
img_sepia_array = np.stack([new_r, new_g, new_b], axis=2)
# Aseguramos que los valores sean enteros y no superen 255.
img_sepia_array = np.clip(img_sepia_array, 0, 255).astype('uint8')


# -----------------------------------------------------------
# EXPORTACIÓN: Guardar la Matriz como Archivo
# -----------------------------------------------------------

# Convertimos la matriz NumPy de vuelta a un objeto de Imagen PIL
img_sepia_pil = Image.fromarray(img_sepia_array)

# Usamos la función .save() para escribir el archivo en el disco.
NOMBRE_ARCHIVO_SALIDA = "foto_sepia_output.jpg"
img_sepia_pil.save(NOMBRE_ARCHIVO_SALIDA)

print(f"3. ✅ ¡Transformación completa y guardada como: {NOMBRE_ARCHIVO_SALIDA}")

# 5. VISUALIZACIÓN (Opcional, pero útil)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1); plt.imshow(img); plt.title("Original")
plt.subplot(1, 2, 2); plt.imshow(img_sepia_array); plt.title("Sepia Generada")
plt.show()
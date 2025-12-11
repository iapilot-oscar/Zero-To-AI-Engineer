import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# 1. CARGA
img = Image.open('foto.jpg').convert('L') 
matriz = np.array(img)
alto, ancho = matriz.shape

# 2. DEFINICIÓN DE KERNELS (LOS DOS OJOS)
# Detector Vertical (Izquierda vs Derecha)
kernel_gx = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]
])

# Detector Horizontal (Arriba vs Abajo)
kernel_gy = np.array([
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1]
])

# Lienzo final
imagen_final = np.zeros((alto, ancho))

print("Procesando ambos ejes (X e Y)...")

# 3. EL BUCLE MAESTRO
for y in range(1, alto - 1):
    for x in range(1, ancho - 1):
        
        # A. Recorte (Slicing) - Solo lo hacemos una vez
        region = matriz[y-1:y+2, x-1:x+2]
        
        # B. Aplicamos Kernel Vertical
        val_v = np.sum(region * kernel_gx)
        
        # C. Aplicamos Kernel Horizontal
        val_h = np.sum(region * kernel_gy)
        
        # D. Fusión (Pitágoras)
        # Calculamos la magnitud del vector gradiente
        magnitud = np.sqrt(val_v**2 + val_h**2)
        
        imagen_final[y, x] = magnitud

# 4. RESULTADO
# Normalizamos para que se vea bien (dividimos por el máximo para tener 0 a 1, o clip a 255)
imagen_final = imagen_final / np.max(imagen_final) * 255

plt.figure(figsize=(10, 10))
plt.imshow(imagen_final, cmap='gray')
plt.title("Detector de Bordes Completo (Sobel)")
plt.axis('off')
plt.show()
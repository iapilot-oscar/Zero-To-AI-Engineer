import numpy as np
from PIL import Image

# 1. Cargar TU archivo real
img = np.array(Image.open("foto.jpg"))

# 2. Obtener las dimensiones reales
# img.shape devuelve (Alto, Ancho, Canales)
alto_real = img.shape[0]   # Filas
ancho_real = img.shape[1]  # Columnas

# 3. Calcular el total de pixeles (El Área)
total_pixeles = alto_real * ancho_real

print(f"--- INFORME DE DIMENSIONES ---")
print(f"Alto (Filas):      {alto_real}")
print(f"Ancho (Columnas):  {ancho_real}")
print(f"-----------------------------")
print(f"TOTAL DE PIXELES:  {total_pixeles}")
print(f"-----------------------------")
print(f"OPERACIONES REALIZADAS: {total_pixeles * 3}")
print(f"(Porque cada pixel tiene 3 canales R, G, B que se calculan por separado)")

# 1. Cargar tu imagen
img = np.array(Image.open("foto.jpg"))

# 2. DEFINIR COORDENADAS (El "GPS" del pixel)
# Nota: En Python empezamos a contar desde 0.
# Pixel [1,1] es la segunda fila, segunda columna.
fila = 1
columna = 1

# 3. EXTRAER EL VALOR
# Accedemos a la matriz en la dirección [fila, columna]
# Esto nos devuelve una lista de 3 números: [R, G, B]
pixel_elegido = img[fila, columna]

print(f"--- INSPECCIÓN DEL PIXEL [{fila}, {columna}] ---")
print(f"Valores encontrados: {pixel_elegido}")
print(f"🔴 Intensidad Roja:  {pixel_elegido[0]}")
print(f"🟢 Intensidad Verde: {pixel_elegido[1]}")
print(f"🔵 Intensidad Azul:  {pixel_elegido[2]}")

print("\n--------------------------------------")

# Vamos a ver también un pixel del centro para comparar
centro_fila = img.shape[0] // 2
centro_col = img.shape[1] // 2
pixel_centro = img[centro_fila, centro_col]

print(f"--- INSPECCIÓN DEL PIXEL CENTRAL [{centro_fila}, {centro_col}] ---")
print(f"Valores encontrados: {pixel_centro}")
print(f"🔴 R: {pixel_centro[0]}  |  🟢 G: {pixel_centro[1]}  |  🔵 B: {pixel_centro[2]}")
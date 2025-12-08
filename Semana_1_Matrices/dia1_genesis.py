import numpy as np
import matplotlib.pyplot as plt
# 1. CREACION DEL VACIO 
# np.zeros crea la matriz
# El primer argumento es la forma (Shape): (Alto/Filas, Ancho/Columnas) -> (500, 500)
# (Alto, Ancho, Canales) -> 3 Canales (Red, Green, Blue)
# dtype='uint8' fuerza a que los numeros sean enteros de 8 bits (0 a 255). img = np.zeros((500,500), dtype='unint8')

img = np.zeros((500, 500, 3), dtype='uint8')

linea_de_color = np.linspace(0, 255, 500)
img[:, :, 2] = linea_de_color

# 2. VISUALIZACION
# plt.imshow interpreta la matriz como imagen.
# cmap='gray' es CRITICO: le dice a python que '0' es negro y el maximo es blanco.
# vmin=0, vmax=255 asegura que la escala sea absoluta (0=negro, 255=blanco) y no relativa a los datos 
plt.imshow(img, cmap='gray', vmin=0, vmax=255)

# 3. EJECUCION GRAFICA 
# Abre la ventana con el resultado.
plt.show()
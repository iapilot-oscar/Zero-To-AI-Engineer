import numpy as np
import matplotlib.pyplot as plt

# 1. Lienzo en blanco 
# El primer argumento es la forma (Shape): (Alto/Filas, Ancho/Columnas) -> (500, 500)
# (Alto, Ancho, Canales) -> 3 Canales (Red, Green, Blue)
# dtype='uint8' fuerza a que los numeros sean enteros de 8 bits (0 a 255). img = np.zeros((500,500), dtype='unint8')

img = np.zeros((500, 500, 3), dtype='uint8')
img[:] = 255 # truco rapido para pintar todo de blanco

# 2. GENERAR EL SISTEMA DE COORDENADAS
# Y, X son matrices que guardan la posicion de cada pixel 
y, x = np.ogrid[:500, :500]


# --- AQUI EMPIEZA TU TRABAJO ---
# 3. La Mascara (El cerebro Matematico)
# Necesitamos saber que pixeles estan dentro del circulo.
centro_y, centro_x = 250, 250
radio_al_cuadrado = 100 ** 2 # RAdio de 100 piexeles.

# Esta linea crea una matriz de Verdad/Mentira (True/False)
# Si la distancia al cuadrado es menor al radio, es True (esta dentro).
mascara_circulo = (x - centro_x)**2 + (y - centro_y)**2 < radio_al_cuadrado

# 4. PINTAR USANDO LA MASCARA
# "Donde la mascara sea verdadera, pinta el pixel de Rojo (255, 0, 0)"
img[mascara_circulo] = [255, 0, 0]

plt.imshow(img)
plt.show()
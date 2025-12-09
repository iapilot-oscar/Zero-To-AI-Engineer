import numpy as np
from PIL import Image

# -----------------------------------------------------------
# CONFIGURACIÓN DE AUDITORÍA
# -----------------------------------------------------------

# 1. CARGAR LA IMAGEN DE GRISES (la que acabamos de guardar)
try:
    # Carga la imagen que acabas de generar
    img_gris_audit = np.array(Image.open("foto_gris_output2.png"))
except FileNotFoundError:
    print("❌ ERROR: El archivo 'foto_gris_output2.png' no fue encontrado.")
    print("Asegúrate de ejecutar primero el código de transformación a grises.")
    exit()

# Definición de coordenadas y valores esperados
CENTRO_FILA = 2093
CENTRO_COLUMNA = 2791

# Valor esperado: 122 (del cálculo: 365 / 3 = 121.666... -> 122)
VALOR_GRIS_ESP = 122 

# -----------------------------------------------------------
# 2. AUDITORÍA DEL PIXEL CENTRAL [2093, 2791]
# -----------------------------------------------------------
pixel_centro_gris = img_gris_audit[CENTRO_FILA, CENTRO_COLUMNA]

print(f"\n--- 🕵️‍♂️ AUDITORÍA PIXEL CENTRAL GRIS ---")
print(f"VALOR ÚNICO ESPERADO: {VALOR_GRIS_ESP}")
print(f"VALORES OBTENIDOS POR CÓMPUTO: {pixel_centro_gris}")

print(f"  🔴 Canal Rojo:  {pixel_centro_gris[0]} (Debe ser {VALOR_GRIS_ESP})")
print(f"  🟢 Canal Verde: {pixel_centro_gris[1]} (Debe ser {VALOR_GRIS_ESP})")
print(f"  🔵 Canal Azul:  {pixel_centro_gris[2]} (Debe ser {VALOR_GRIS_ESP})")
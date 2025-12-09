import numpy as np
from PIL import Image

# -----------------------------------------------------------
# CONFIGURACIÓN DE AUDITORÍA
# -----------------------------------------------------------

# 1. CARGAR LA IMAGEN SEPIA (la que acabamos de guardar)
try:
    img_sepia_audit = np.array(Image.open("foto_sepia_output.jpg"))
except FileNotFoundError:
    print("❌ ERROR: El archivo 'foto_sepia_output.jpg' no fue encontrado.")
    print("Asegúrate de ejecutar primero 'dia2_sepia_maker.py'.")
    exit()

# Definición de coordenadas y valores esperados (de nuestro cálculo manual)
CENTRO_FILA = 2093
CENTRO_COLUMNA = 2791

# --- VALORES ESPERADOS ---
R_ESP_1_1, G_ESP_1_1, B_ESP_1_1 = 140, 125, 97  # Valores esperados para el pixel [1, 1]
R_ESP_CENTRO, G_ESP_CENTRO, B_ESP_CENTRO = 172, 153, 119 # Valores esperados para el pixel central

# -----------------------------------------------------------
# 2. AUDITORÍA DEL PIXEL [1, 1]
# -----------------------------------------------------------
pixel_1_1_sepia = img_sepia_audit[1, 1]

print("\n--- 🕵️‍♂️ AUDITORÍA PIXEL [1, 1] ---")
print(f"VALORES ESPERADOS (Manual): [R:{R_ESP_1_1}, G:{G_ESP_1_1}, B:{B_ESP_1_1}]")
print(f"VALORES OBTENIDOS POR CÓMPUTO: {pixel_1_1_sepia}")

# -----------------------------------------------------------
# 3. AUDITORÍA DEL PIXEL CENTRAL [2093, 2791]
# -----------------------------------------------------------
pixel_centro_sepia = img_sepia_audit[CENTRO_FILA, CENTRO_COLUMNA]

print(f"\n--- 🕵️‍♂️ AUDITORÍA PIXEL CENTRAL ---")
print(f"VALORES ESPERADOS (Manual): [R:{R_ESP_CENTRO}, G:{G_ESP_CENTRO}, B:{B_ESP_CENTRO}]")
print(f"VALORES OBTENIDOS POR CÓMPUTO: {pixel_centro_sepia}")
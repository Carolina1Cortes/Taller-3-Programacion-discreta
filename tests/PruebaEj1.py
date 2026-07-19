import sys
import os

# Configuración de rutas para importar tu módulo
carpeta_actual = os.path.dirname(os.path.abspath(__file__))
ruta_cripto = os.path.join(carpeta_actual, "..", "src", "cripto")
sys.path.append(ruta_cripto)

from CifradoCesar import cifrar, descifrar, fuerzabruta

print("==================================================================")
# Explicación del propósito de este archivo
print("   DEMOSTRACIÓN Y BANCO DE PRUEBAS: CIFRADO CÉSAR ")
print("   (Verificación visual de resultados y transformaciones)")
print("==================================================================\n")

# 1. Pruebas de Cifrado
print("--- 1. PRUEBAS DE LA FUNCIÓN: cifrar(texto, k) ---")
casos_cifrar = [
    ("HOLA UNAL", 3),
    ("Hola, mundo!", 5),
    ("PRUEBA", 0),
    ("PRUEBA", 26),
    ("TEXTO EN MINUSCULAS", 10),
    ("Cifrado con k negativo", -3)
]
    
for texto, k in casos_cifrar:
    resultado = cifrar(texto, k)
    print(f"-> Entrada: '{texto}' | Clave k = {k}")
    print(f"   Resultado obtenido: '{resultado}'")

# 2. Pruebas de Descifrado
print("\n--- 2. PRUEBAS DE LA FUNCIÓN: descifrar(texto, k) ---")
casos_descifrar = [
    ("KROD XQDO", 3),
    ("MTQF, RZSJT!", 5),
    ("PRUEBA", 0),
    ("PRUEBA", 26)
]
    
for texto, k in casos_descifrar:
    resultado = descifrar(texto, k)
    print(f"-> Entrada (Cifrada): '{texto}' | Clave k = {k}")
    print(f"   Resultado obtenido:   '{resultado}'")

# 3. Prueba de Consistencia (Ciclo Completo)
print("\n--- 3. PRUEBA DE CONSISTENCIA (Cifrar -> Descifrar) ---")
texto_original = "Matematicas Discretas 2026!"
clave_ejemplo = 7
    
texto_cifrado = cifrar(texto_original, clave_ejemplo)
texto_recuperado = descifrar(texto_cifrado, clave_ejemplo)
    
print(f"Texto Original:   '{texto_original}'")
print(f"Texto Cifrado (k={clave_ejemplo}): '{texto_cifrado}'")
print(f"Texto Recuperado: '{texto_recuperado}'")

# 4. Demostración de Fuerza Bruta
print("\n--- 4. PRUEBA DE LA FUNCIÓN: fuerzabruta(texto) ---")
texto_ataque = "KROD XQDO"
fuerzabruta(texto_ataque)
print("==================================================================")
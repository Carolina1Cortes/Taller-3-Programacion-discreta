import sys
import os

carpeta_actual = os.path.dirname(os.path.abspath(__file__))
ruta_boole = os.path.join(carpeta_actual, "..", "src", "boole")
sys.path.append(ruta_boole)

from Shannon import entropia

# Cada caso: (nombre, texto, entropia_esperada)
casos = [
    ("Texto de un solo símbolo (mínima incertidumbre)", "AAAA", 0.0),
    ("Dos símbolos 50/50 (máxima incertidumbre con 2 símbolos)", "AABB", 1.0),
    ("Cuatro símbolos equiprobables (log2(4)=2)", "ABCD", 2.0),
]

for nombre, texto, esperado in casos:
    resultado = entropia(texto)
    correcto = abs(resultado - esperado) < 0.0001  # tolerancia por decimales

    print(f"Caso: {nombre}")
    print(f"Entrada: '{texto}'")
    print(f"Resultado: {resultado:.4f}")
    print(f"Bien o mal: {'✅ Bien' if correcto else f'❌ Mal (esperaba {esperado})'}")
    print()
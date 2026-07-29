import sys
import os

carpeta_actual = os.path.dirname(os.path.abspath(__file__))
ruta_cripto = os.path.join(carpeta_actual, "..", "src", "cripto")
sys.path.append(ruta_cripto)

from MPC import recontruir_suma_promedio, simular_servidores

# --- Casos válidos: verificamos que la suma y el promedio se reconstruyan bien ---
casos_validos = [
    ("Ejemplo del enunciado", [40, 35, 50, 25], 1000003, 150, 37.5),
    ("Una sola nota", [30], 1000003, 30, 30.0),
    ("Extremos válidos (0 y 50)", [0, 50], 1000003, 50, 25.0),
    ("Ocho notas variadas", [10, 20, 30, 40, 50, 0, 15, 25], 1000003, 190, 23.75),
]

print("--- Casos válidos ---\n")
for nombre, notas, M, suma_esperada, promedio_esperado in casos_validos:
    suma, promedio = recontruir_suma_promedio(notas, M)
    correcto = (suma == suma_esperada and promedio == promedio_esperado)

    print(f"Caso: {nombre}")
    print(f"Entrada: notas={notas}, M={M}")
    print(f"Resultado: suma={suma}, promedio={promedio}")
    print(f"Bien o mal: {'✅ Bien' if correcto else f'❌ Mal (esperaba suma={suma_esperada}, promedio={promedio_esperado})'}")
    print()

# --- Casos que deben detectar error (simular_servidores debe devolver None) ---
casos_error = [
    ("Nota fuera de rango por arriba", [40, 60, 25], 1000003),
    ("Nota fuera de rango por abajo", [40, -5, 25], 1000003),
    ("Lista vacía", [], 1000003),
]

print("--- Casos que deben fallar ---\n")
for nombre, notas, M in casos_error:
    resultado = simular_servidores(notas, M)
    correcto = resultado is None

    print(f"Caso: {nombre}")
    print(f"Entrada: notas={notas}, M={M}")
    print(f"Resultado: {resultado}")
    print(f"Bien o mal: {'✅ Bien' if correcto else '❌ Mal (debía devolver None)'}")
    print()
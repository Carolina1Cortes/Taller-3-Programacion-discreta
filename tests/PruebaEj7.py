import sys
import os

carpeta_actual = os.path.dirname(os.path.abspath(__file__))
ruta_boole = os.path.join(carpeta_actual, "..", "src", "boole")
sys.path.append(ruta_boole)

from TablasVerdad import *

# Cada caso: (nombre, función, valores de entrada, resultado esperado)
casos = [
    ("expre1 (1 var, ¬A) con A=0", expre1, (0,), True),
    ("expre1 (1 var, ¬A) con A=1", expre1, (1,), False),
    ("expre2 (2 var, A⊕B) con A=1,B=0", expre2, (1, 0), True),
    ("expre2 (2 var, A⊕B) con A=1,B=1", expre2, (1, 1), False),
    ("expre3 (3 var) con A=1,B=1,C=1", expre3, (1, 1, 1), True),
    ("expre3 (3 var) con A=0,B=0,C=0", expre3, (0, 0, 0), True),
    ("expre3 (3 var) con A=1,B=0,C=1", expre3, (1, 0, 1), False),
    ("expre5 (3 var) con A=1,B=0,C=1", expre5, (1, 0, 1), True),
    ("expre5 (3 var) con A=1,B=1,C=1", expre5, (1, 1, 1), False),
    ("expre8 (4 var) con A=1,B=1,C=0,D=0", expre8, (1, 1, 0, 0), True),
    ("expre8 (4 var) con A=0,B=0,C=1,D=1", expre8, (0, 0, 1, 1), False),
]

for nombre, expresion, entrada, esperado in casos:
    resultado = evaluar_entrada(expresion, *entrada)
    correcto = (resultado == esperado)

    print(f"Caso: {nombre}")
    print(f"Entrada: {entrada}")
    print(f"Resultado: {resultado}")
    print(f"Bien o mal: {'✅ Bien' if correcto else f'❌ Mal (esperaba {esperado})'}")
    print()
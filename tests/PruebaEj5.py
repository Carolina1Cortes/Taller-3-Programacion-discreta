import sys
import os

carpeta_actual = os.path.dirname(os.path.abspath(__file__))
ruta_grafos = os.path.join(carpeta_actual, "..", "src", "grafos")
sys.path.append(ruta_grafos)

from CierreEstacion import comparar_antes_despues
from dijkstra import grafo_ejemplo

grafo = grafo_ejemplo()
pares = [
    ("Portal", "Terminal"),
    ("Portal", "Estadio"),
    ("Museo", "Parque"),
    ("Calle26", "Terminal"),
    ("Centro", "Estadio"),
]
cierre = {"vertice": "Centro"}

# (origen, destino, antes_esperado, despues_esperado, estado_esperado)
casos_esperados = [
    ("Portal", "Terminal", 21, 24, "conectado"),
    ("Portal", "Estadio", 17, 20, "conectado"),
    ("Museo", "Parque", 9, 16, "conectado"),
    ("Calle26", "Terminal", 19, 19, "conectado"),
    ("Centro", "Estadio", 9, None, "desconectado"),
]

resultados = comparar_antes_despues(grafo, pares, cierre)

for r, (origen, destino, antes_esp, despues_esp, estado_esp) in zip(resultados, casos_esperados):
    correcto = (
        r["distancia_antes"] == antes_esp
        and r["distancia_despues"] == despues_esp
        and r["estado"] == estado_esp
    )
    print(f"Caso: {origen} -> {destino}")
    print(f"Resultado: antes={r['distancia_antes']}, despues={r['distancia_despues']}, estado={r['estado']}")
    print(f"Bien o mal: {'✅ Bien' if correcto else '❌ Mal'}")
    print()
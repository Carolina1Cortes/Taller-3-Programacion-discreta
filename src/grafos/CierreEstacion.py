import sys
import os
import copy

carpeta_actual = os.path.dirname(os.path.abspath(__file__))
sys.path.append(carpeta_actual)

from dijkstra import dijkstra, grafo_ejemplo


def eliminar_vertice(grafo, vertice):
    #Devuelve una COPIA del grafo sin el vértice dado (y sin aristas hacia él).
    nuevo_grafo = copy.deepcopy(grafo)
    nuevo_grafo.pop(vertice, None)
    for v in nuevo_grafo:
        nuevo_grafo[v].pop(vertice, None)  # el grafo de tu compañero usa dict, no lista
    return nuevo_grafo


def eliminar_arista(grafo, a, b):
    #Devuelve una COPIA del grafo sin la arista entre a y b (en ambos sentidos).
    nuevo_grafo = copy.deepcopy(grafo)
    if a in nuevo_grafo:
        nuevo_grafo[a].pop(b, None)
    if b in nuevo_grafo:
        nuevo_grafo[b].pop(a, None)
    return nuevo_grafo


def comparar_antes_despues(grafo, pares, cierre):
    """
    cierre: {"vertice": "X"} o {"arista": ("A", "B")}
    Devuelve una lista de dicts con: origen, destino, antes, despues, diferencia, estado.
    """
    if "vertice" in cierre:
        grafo_nuevo = eliminar_vertice(grafo, cierre["vertice"])
    else:
        a, b = cierre["arista"]
        grafo_nuevo = eliminar_arista(grafo, a, b)

    resultados = []
    for origen, destino in pares:
        antes, _ = dijkstra(grafo, origen, destino)
        despues, _ = dijkstra(grafo_nuevo, origen, destino)

        if despues is None:
            estado = "desconectado"
            diferencia = None
        else:
            estado = "conectado"
            diferencia = despues - antes

        resultados.append({
            "origen": origen,
            "destino": destino,
            "distancia_antes": antes,
            "distancia_despues": despues,
            "diferencia": diferencia,
            "estado": estado,
        })
    return resultados


def imprimir_tabla(resultados):
    print(f"{'Origen':<12}{'Destino':<12}{'Antes':<8}{'Después':<10}{'Diferencia':<12}{'Estado'}")
    print("-" * 65)
    for r in resultados:
        despues = r["distancia_despues"] if r["distancia_despues"] is not None else "—"
        diferencia = r["diferencia"] if r["diferencia"] is not None else "—"
        print(f"{r['origen']:<12}{r['destino']:<12}{r['distancia_antes']:<8}{despues!s:<10}{diferencia!s:<12}{r['estado']}")


if __name__ == "__main__":
    grafo = grafo_ejemplo()

    pares = [
        ("Portal", "Terminal"),
        ("Portal", "Estadio"),
        ("Museo", "Parque"),
        ("Calle26", "Terminal"),
        ("Centro", "Estadio"),
    ]

    # Cierre de ejemplo: eliminamos el vértice "Centro"
    cierre = {"vertice": "Centro"}

    resultados = comparar_antes_despues(grafo, pares, cierre)
    print(f"Cierre simulado: {cierre}\n")
    imprimir_tabla(resultados)
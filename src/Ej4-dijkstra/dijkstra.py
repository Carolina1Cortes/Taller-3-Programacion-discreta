import json
import heapq

def construir_grafo():
    grafo = {}
    return grafo

def agregar_arista(grafo, origen, destino, peso):
    grafo.setdefault(origen, {})[destino] = peso
    grafo.setdefault(destino, {})[origen] = peso

def dijkstra(grafo, inicio, fin):
    dist = {v: math_inf() for v in grafo}
    dist[inicio] = 0
    prev = {v: None for v in grafo}
    visitados = set()
    cola = [(0, inicio)]
    while cola:
        d, u = heapq.heappop(cola)
        if u in visitados:
            continue
        visitados.add(u)
        if u == fin:
            break
        for v, peso in grafo.get(u, {}).items():
            nd = d + peso
            if nd < dist[v]:
                dist[v] = nd
                prev[v] = u
                heapq.heappush(cola, (nd, v))
    if dist.get(fin, math_inf()) == math_inf():
        return None, []
    ruta = []
    actual = fin
    while actual is not None:
        ruta.append(actual)
        actual = prev[actual]
    ruta.reverse()
    return dist[fin], ruta

def math_inf():
    return float("inf")

ARISTAS_DE_EJEMPLO = [
    ("Portal", "Calle26", 5),
    ("Portal", "Centro", 8),
    ("Calle26", "Museo", 4),
    ("Calle26", "Universidad", 7),
    ("Museo", "Centro", 3),
    ("Centro", "Universidad", 2),
    ("Centro", "Parque", 6),
    ("Universidad", "Parque", 5),
    ("Universidad", "Estadio", 9),
    ("Parque", "Estadio", 3),
    ("Parque", "Terminal", 7),
    ("Estadio", "Terminal", 4),
]

def grafo_ejemplo():
    grafo = {}
    for o, d, p in ARISTAS_DE_EJEMPLO:
        agregar_arista(grafo, o, d, p)
    return grafo

def mostrar_aristas_ejemplo():
    print("ARISTAS_DE_EJEMPLO = [")
    for o, d, p in ARISTAS_DE_EJEMPLO:
        print(f'    ("{o}", "{d}", {p}),')
    print("]")

def cargar_json():
    nombre = input("Nombre del archivo (misma carpeta): ")
    try:
        with open(nombre, "r", encoding="utf-8") as f:
            datos = json.load(f)
    except Exception as e:
        print(f"Error: {e}")
        return None
    grafo = {}
    for arista in datos:
        agregar_arista(grafo, arista["origen"], arista["destino"], arista["peso"])
    return grafo

def cargar_terminal():
    grafo = construir_grafo()
    print("Formato: origen,destino,peso")
    while True:
        print("\n1. Agregar arista")
        print("2. Terminar")
        op = input("Opcion: ")
        if op == "1":
            linea = input("origen,destino,peso: ")
            try:
                o, d, p = linea.split(",")
                agregar_arista(grafo, o.strip(), d.strip(), float(p.strip()))
            except Exception:
                print("Formato invalido.")
        elif op == "2":
            break
        else:
            print("Opcion invalida.")
    return grafo

def ejecutar_dijkstra(grafo):
    if not grafo:
        print("Grafo vacio.")
        return
    print(f"Vertices: {list(grafo.keys())}")
    inicio = input("Vertice origen: ")
    fin = input("Vertice destino: ")
    if inicio not in grafo or fin not in grafo:
        print("Vertice no existe.")
        return
    dist, ruta = dijkstra(grafo, inicio, fin)
    if dist is None:
        print("No hay ruta.")
    else:
        print(f"Distancia total: {dist}")
        print(f"Ruta: {' -> '.join(ruta)}")

def menu():
    while True:
        print("\n=== Dijkstra Taller ===")
        print("1. Grafo de ejemplo")
        print("2. Cargar grafo JSON")
        print("3. Cargar grafo por terminal")
        print("0. Salir")
        op = input("Opcion: ")
        if op == "1":
            mostrar_aristas_ejemplo()
            ejecutar_dijkstra(grafo_ejemplo())
        elif op == "2":
            g = cargar_json()
            if g:
                ejecutar_dijkstra(g)
        elif op == "3":
            ejecutar_dijkstra(cargar_terminal())
        elif op == "0":
            break
        else:
            print("Opcion invalida.")

if __name__ == "__main__":
    menu()

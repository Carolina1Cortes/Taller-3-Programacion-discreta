# Ejercicio 5 — Cierre de una estación: medir el impacto en la red

## 1. ¿Qué problema resuelve el programa?
Mide el impacto de cerrar un vértice o una arista de una red de
transporte, comparando las rutas más cortas entre varios pares de
puntos antes y después del cierre.

## 2. ¿Qué idea matemática usa?
Reutiliza el algoritmo de Dijkstra (ejercicio 4) sobre el mismo grafo,
ejecutándolo dos veces: una sobre el grafo original y otra sobre una
copia sin el vértice/arista cerrado. Si el elemento eliminado no
formaba parte del camino más corto de un par, la distancia no cambia.
Si sí formaba parte, la nueva ruta (si existe) es igual o más larga,
porque de haber una más corta ya habría sido la original. Si no queda
ninguna ruta alternativa, el par se reporta como desconectado.

## 3. ¿Cómo se ejecuta?
Desde la carpeta `src/grafos/`:
```bash
python CierreEstacion.py
```
Usa el grafo de ejemplo del ejercicio 4 y simula el cierre del vértice
"Centro", mostrando una tabla con origen, destino, distancia antes,
distancia después, diferencia y estado para 5 pares de prueba.

## 4. ¿Qué pruebas hicieron?
En `tests/PruebaEj5.py` se compararon los 5 pares contra los valores
observados al correr el programa, incluyendo un caso donde el cierre no
afecta la distancia (Calle26-Terminal, diferencia 0) y un caso donde el
par queda completamente desconectado (Centro-Estadio, al eliminar el
propio vértice Centro).

## 5. ¿Qué limitaciones tiene la solución?
- Solo simula el cierre de un vértice o arista a la vez; no evalúa
  cierres múltiples simultáneos.
- Depende directamente de la implementación de Dijkstra del ejercicio 4
  (mismo archivo `dijkstra.py`), así que cualquier cambio en su formato
  de grafo (dict de diccionarios) requiere ajustar también este ejercicio.
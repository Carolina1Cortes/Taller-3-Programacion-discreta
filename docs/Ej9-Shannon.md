# Ejercicio 9 — Shannon: medir información en un mensaje

## 1. ¿Qué problema resuelve el programa?
Calcula qué tan incierto o predecible es un texto, usando la entropía
de Shannon, y compara la entropía de dos textos distintos.

## 2. ¿Qué idea matemática usa?
La entropía de Shannon se calcula como:

    H = -Σ p_i · log2(p_i)

donde p_i es la probabilidad de cada símbolo (su frecuencia dividida
entre el total de símbolos del texto). Un texto con un solo símbolo
repetido tiene entropía 0 (no hay ninguna incertidumbre: siempre sabes
qué símbolo sigue). Un texto donde todos los símbolos son igual de
probables tiene la entropía máxima posible para esa cantidad de
símbolos (log2(n) para n símbolos equiprobables).

La entropía mide incertidumbre promedio por símbolo, NO la longitud
del texto: un texto largo pero muy repetitivo puede tener menor
entropía que uno corto pero variado.

## 3. ¿Cómo se ejecuta?
Desde la carpeta `src/boole/`:
```bash
python Shannon.py
```
Muestra las frecuencias y probabilidades de un texto de ejemplo, y
compara la entropía de un texto repetitivo contra uno variado.

## 4. ¿Qué pruebas hicieron?
En `tests/PruebaEj9.py` se verificaron 3 casos con valores matemáticos
conocidos: un texto de un solo símbolo (entropía 0), dos símbolos en
proporción 50/50 (entropía 1), y cuatro símbolos equiprobables
(entropía 2 = log2(4)).

## 5. ¿Qué limitaciones tiene la solución?
- No implementa la extensión opcional de código Huffman.
- Trata cada carácter (incluyendo espacios y signos de puntuación)
  como un símbolo independiente; no distingue mayúsculas de minúsculas
  como símbolos distintos ni agrupa por palabras.
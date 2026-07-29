# Algoritmo voraz para coloreado de grafos

## ¿Por qué el algoritmo voraz no siempre garantiza el menor número de colores?

El algoritmo voraz asigna a cada vértice el primer color disponible en
el momento en que lo procesa. Esta decisión se toma utilizando
únicamente la información local, es decir, los colores de los vértices
vecinos que ya fueron coloreados.

Debido a que no analiza todas las posibles combinaciones de coloreado,
el resultado depende del orden en que se procesen los vértices. Un orden
diferente puede requerir menos colores para el mismo grafo. Por esta
razón, el algoritmo voraz no garantiza obtener el número mínimo posible
de colores (número cromático).

## ¿Por qué sí produce una asignación válida?

Aunque no siempre utiliza la menor cantidad de colores, el algoritmo
genera una asignación válida cuando está correctamente implementado.

En este programa, antes de asignar un color a un vértice, se identifican
los colores utilizados por sus vecinos ya coloreados y se selecciona el
primer color que no produzca conflictos. De esta manera, dos vértices
adyacentes nunca reciben el mismo color.

Además, la función `verificar_coloreado()` recorre todas las aristas del
grafo para comprobar que no existan vértices vecinos con el mismo color.
Si esta verificación es correcta, el coloreado obtenido es válido.

## Relación con el programa

La función `colorear_grafo_voraz()` ordena inicialmente los vértices
según su grado y asigna el primer color disponible a cada uno.
Posteriormente, `verificar_coloreado()` confirma que cada par de
vértices conectados posee colores diferentes, garantizando así una
solución válida aunque no necesariamente óptima en el número de colores
utilizados.

# Explicación sobre Dijkstra

## ¿Por qué Dijkstra necesita pesos no negativos?

El algoritmo de Dijkstra supone que, una vez selecciona el vértice con
la menor distancia acumulada, dicha distancia ya es la mínima posible y
no volverá a mejorar. Esta propiedad solo se cumple cuando todas las
aristas tienen pesos iguales o mayores que cero.

Si existieran pesos negativos, podría encontrarse posteriormente un
camino con menor costo hacia un vértice que ya fue marcado como
definitivo. En ese caso, el algoritmo produciría resultados incorrectos.

En el programa, los pesos de las aristas representan costos o distancias
y se acumulan durante la búsqueda del camino mínimo. El algoritmo
compara continuamente estos costos para actualizar la mejor ruta
encontrada.

## ¿Qué significa que un camino sea óptimo?

Un camino óptimo es la ruta cuyo costo total es el menor posible entre
un vértice de origen y uno de destino.

En Dijkstra, el costo total corresponde a la suma de los pesos de todas
las aristas que forman la ruta. Durante la ejecución, el algoritmo
evalúa diferentes caminos y conserva únicamente el de menor costo para
cada vértice.

Cuando finaliza, la distancia obtenida y la secuencia de vértices
reconstruida representan el camino óptimo, es decir, la ruta con el
menor costo acumulado entre el origen y el destino.

## Relación con el programa

En la función `dijkstra()`, la distancia mínima conocida para cada
vértice se almacena en el diccionario `dist`. Cada vez que se encuentra
un camino de menor costo, se actualizan `dist` y `prev`, lo que permite
reconstruir al final la ruta óptima encontrada.

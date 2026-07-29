# Minterminos y equivalencia de expresiones booleanas

## ¿Qué es un mintermino?

Un mintermino es un producto lógico (AND) que incluye todas las
variables de una función booleana, ya sea en forma directa o
complementada. Cada mintermino representa una única combinación de
valores de entrada para la cual la función toma el valor 1.

En el programa, los minterminos se identifican mediante su índice
decimal y se convierten a su representación lógica con la función
`minterm_to_term()`, que genera la expresión correspondiente a cada
combinación binaria.

## ¿Por qué dos expresiones son equivalentes si tienen la misma tabla de verdad?

Dos expresiones booleanas son equivalentes cuando producen exactamente
el mismo resultado para todas las posibles combinaciones de sus
variables de entrada.

La tabla de verdad contiene todas esas combinaciones posibles y el valor
de salida asociado a cada una. Si dos expresiones generan la misma
salida en todas las filas de la tabla, ambas representan la misma
función lógica, aunque estén escritas de forma diferente.

## Relación con el programa

Después de simplificar la función booleana, el programa construye la
tabla de verdad y compara la expresión original con la expresión
simplificada. Si ambas producen el mismo resultado en todas las
combinaciones de entrada, la simplificación se considera correcta y las
expresiones son lógicamente equivalentes.

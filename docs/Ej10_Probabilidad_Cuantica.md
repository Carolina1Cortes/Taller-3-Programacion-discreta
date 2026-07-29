# Probabilidad cuántica simulada y computador cuántico real

## ¿Qué es la probabilidad cuántica simulada?

La probabilidad cuántica simulada consiste en calcular mediante un
computador clásico las probabilidades de obtener cada estado de un qubit
utilizando modelos matemáticos de la mecánica cuántica. Posteriormente,
el programa genera resultados aleatorios que siguen esas probabilidades.

En este programa, las probabilidades teóricas se obtienen a partir de
los cuadrados de los módulos de las amplitudes `alpha` y `beta`, y
después se simulan 1000 mediciones utilizando la función
`random.choices()`.

## ¿Qué ocurre en un computador cuántico real?

En un computador cuántico real no se simulan los resultados mediante
números aleatorios. El qubit existe físicamente en un estado de
superposición y, al realizar una medición, la mecánica cuántica
determina el resultado con las probabilidades dadas por sus amplitudes.

Cada ejecución corresponde a una medición física del sistema cuántico,
por lo que los resultados están sujetos a fenómenos reales como ruido,
decoherencia y errores experimentales.

## Diferencias principales

-   En una simulación, todos los cálculos se realizan mediante software
    sobre un computador clásico.
-   En un computador cuántico, las operaciones actúan sobre qubits
    físicos mediante compuertas cuánticas reales.
-   La simulación utiliza un generador de números aleatorios para imitar
    las mediciones, mientras que un computador cuántico obtiene los
    resultados directamente del comportamiento físico del sistema.
-   Un simulador puede reproducir el comportamiento esperado de pocos
    qubits, pero su costo computacional aumenta rápidamente conforme
    crece el número de qubits, mientras que un computador cuántico está
    diseñado para procesarlos de manera natural.

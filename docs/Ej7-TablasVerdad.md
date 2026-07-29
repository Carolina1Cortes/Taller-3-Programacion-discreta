# Ejercicio 7 — Tablas de verdad y circuitos lógicos

## 1. ¿Qué problema resuelve el programa?
El programa genera la tabla de verdad completa de una expresión booleana
(mostrando el resultado para todas las combinaciones posibles de sus
variables), y también permite evaluar la expresión en una sola entrada
concreta sin generar la tabla completa. Incluye un menú interactivo que
valida las entradas del usuario.

## 2. ¿Qué idea matemática usa?
Una tabla de verdad recorre **todas** las combinaciones posibles de 0/1
para las variables de una expresión booleana. Con n variables existen
2ⁿ combinaciones — por eso una expresión de 3 variables tiene 8 filas,
y una de 4 variables tiene 16.

Cada operador booleano corresponde a una compuerta lógica real en
electrónica digital: AND, OR, NOT y XOR se combinan para formar
expresiones más complejas, de la misma forma en que las compuertas se
combinan para formar un circuito. La tabla de verdad de una expresión
es, en ese sentido, la especificación exacta del comportamiento que
debería tener el circuito construido con esas compuertas.

Para generar las combinaciones se usa `itertools.product([0,1],
repeat=n)`, que produce automáticamente las 2ⁿ tuplas posibles sin
tener que escribirlas a mano.

## 3. ¿Cómo se ejecuta?
Desde la carpeta `src/boole/`:
```bash
python TablasVerdad.py
```
El programa muestra un menú con dos opciones:
1. Ver la tabla de verdad completa de una expresión.
2. Evaluar la expresión en una entrada concreta (valores específicos
   de A, B, C, D).

En ambos casos, primero se listan las expresiones disponibles con su
notación matemática, y el programa valida que el nombre ingresado
exista, que los valores sean números, que la cantidad de valores
coincida con el número de variables de la expresión elegida, y que
cada valor sea 0 o 1.

## 4. ¿Qué pruebas hicieron?
En `tests/PruebaEj7.py` se probó `evaluar_entrada` sobre expresiones de
1, 2, 3 y 4 variables (para confirmar que la solución generaliza más
allá del mínimo de 3-4 que pide el enunciado), incluyendo casos donde
el resultado esperado es verdadero y casos donde es falso, para
verificar ambas ramas de cada expresión.

Además, se probó manualmente el manejo de errores del menú interactivo:
nombres de expresión inválidos, texto no numérico donde se esperaba un
número, cantidad incorrecta de valores, y valores fuera del rango 0/1
(por ejemplo, ingresar 9 en vez de 0 o 1) — en todos los casos el
programa vuelve a pedir la entrada en vez de fallar o dar un resultado
sin sentido.

## 5. ¿Qué limitaciones tiene la solución?
- El programa solo evalúa expresiones que ya están definidas de
  antemano en el código (como funciones lambda); no permite que el
  usuario escriba una expresión booleana nueva en tiempo de ejecución.
- Aceptar 9 como si fuera "verdadero" en Python (porque cualquier
  número distinto de 0 se comporta como verdadero) es un
  comportamiento del lenguaje que hubo que validar explícitamente
  para que las entradas se restrinjan de verdad a 0 y 1.
# Ejercicio 3 — MPC básico: calcular un promedio sin mostrar los datos

## 1. ¿Qué problema resuelve el programa?
El programa simula un protocolo de computación multipartita segura (MPC)
que permite calcular la suma y el promedio de una lista de notas sin que
ningún servidor individual conozca ninguna nota completa. Solo se revela
el resultado agregado (suma/promedio), nunca los datos individuales.

## 2. ¿Qué idea matemática usa?
Se basa en **secret sharing aditivo** sobre aritmética modular (Z_M, con
M = 1.000.003). Cada nota x se divide en 3 partes:

    s1 = número aleatorio
    s2 = número aleatorio
    s3 = (x - s1 - s2) mod M

de forma que:

    s1 + s2 + s3 ≡ x (mod M)

Cada parte, vista sola, parece un número aleatorio cualquiera: no hay
forma de saber qué nota representa, pues es compatible con *cualquier* valor posible de x, por lo que no
revela ninguna información sobre la nota original. Solo al sumar las tres
partes (algo que ningún servidor puede hacer solo) se recupera x.

Esta propiedad se extiende a listas completas de notas: cada nota se
reparte de forma independiente entre 3 servidores, y al sumar TODO lo que
tiene cada servidor (más el módulo M), los términos aleatorios se cancelan
entre sí y queda exactamente la suma de las notas originales.

## 3. ¿Cómo se ejecuta?
Desde la carpeta `src/cripto/`:
```bash
python MPC.py
```
La función principal es `recontruir_suma_promedio(notas, M)`, que recibe
una lista de notas (enteros entre 0 y 50) y el módulo M, y devuelve/imprime
la suma total y el promedio.

## 4. ¿Qué pruebas hicieron?
En `tests/PruebaEj3.py` se probaron 7 casos, divididos en dos grupos:

**Casos válidos** (verifican que la suma y el promedio se reconstruyan bien):
- El ejemplo del enunciado: `[40, 35, 50, 25]` → suma=150, promedio=37.5
- Una sola nota (caso borde de tamaño de lista)
- Los extremos válidos del rango: notas 0 y 50
- Una lista más grande (8 notas), para confirmar que funciona con
  cualquier tamaño de lista, como exige el enunciado

**Casos que deben fallar** (verifican la validación de errores):
- Una nota por encima de 50
- Una nota negativa
- Una lista vacía (caso borde que además evita una división por cero
  en el cálculo del promedio)

## 5. ¿Qué limitaciones tiene la solución?
- Es una simulación educativa: los 3 "servidores" corren en el mismo
  programa y no hay comunicación real de red ni separación física de
  los datos — en un MPC real, cada servidor estaría en una máquina
  distinta y nunca vería las partes de los demás.
- Solo protege el secreto mientras al menos un servidor no colabore
  con los otros dos: si dos de los tres servidores se ponen de acuerdo
  y comparten sus partes, sí podrían reconstruir la nota original
  (con solo 2 de las 3 partes, siempre existe una combinación posible
  para cualquier valor, así que en realidad hacen falta las 3 — esto
  vale la pena verificarlo si quieren profundizar).
- Las notas deben ser enteros entre 0 y 50; no maneja decimales.
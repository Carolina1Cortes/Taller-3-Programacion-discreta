# Ejercicio 1 — Cifrado César

## 1. ¿Qué problema resuelve el programa?
El programa permite ocultar un mensaje de texto mediante un desplazamiento
fijo de letras (cifrado César), descifrarlo si se conoce ese desplazamiento,
y romperlo por fuerza bruta cuando no se conoce, probando las 26 posibilidades.

## 2. ¿Qué idea matemática usa?
El cifrado César es una operación sobre **Z₂₆** (los enteros módulo 26).
Cada letra se identifica con un número de su posición en el alfabeto
(A=0, B=1, ..., Z=25). Cifrar consiste en sumar el desplazamiento k y
aplicar módulo 26 para que el resultado "dé la vuelta" al llegar al final
del alfabeto:

    cifrado = (posición + k) mod 26

Descifrar es el proceso inverso, restando en vez de sumando:

    descifrado = (posición - k) mod 26

El descifrado funciona porque la resta deshace exactamente la suma que se
aplicó al cifrar — es la operación inversa dentro de Z₂₆.

El ataque de fuerza bruta es posible porque el espacio de claves es muy
pequeño: solo existen 26 valores posibles de k (0 a 25). Un computador
puede probarlos todos en milisegundos, así que basta con generar las 26
versiones del mensaje y que una persona identifique cuál tiene sentido.

## 3. ¿Cómo se ejecuta?
Desde la carpeta `src/cripto/`:
```bash
python CifradoCesar.py
```
El programa pide un texto y un valor de k, y muestra:
- el texto cifrado
- el texto descifrado (para confirmar que vuelve al original)
- las 26 posibilidades de fuerza bruta sobre el texto cifrado

## 4. ¿Qué pruebas hicieron?
En `tests/PruebaEj1.py` se distribuyo la prueba en secciones:
- Pruebas de Cifrado: Evaluó textos estándar(`HOLA UNAL`, k=3), cadenas con caracteres especiales y signos de puntuación (`Hola, mundo!` con k=5) y claves con desplazamientos negativos (k=-3).
- Pruebas de Descifrado: Comprobó la correcta restauración a partir de criptogramas conocidos.
- Casos de Frontera (Borde): Se validó la propiedad de la identidad con $k=0$ (el mensaje no sufre alteración) y la propiedad cíclica del módulo con $k=26$, confirmando matemáticamente que $26 \equiv 0 \pmod{26}$ (una vuelta completa regresa al mismo punto de origen).
- Prueba de Consistencia Lineal: Cifra dinámicamente una cadena mixta y la descifra secuencialmente para corroborar el flujo del criptosistema completo en una sola corrida.
- Simulación de Ataque: Despliega visualmente el comportamiento de la función exhaustiva sobre el criptograma `"KROD XQDO"`.

## 5. ¿Qué limitaciones tiene la solución?
- Solo maneja el alfabeto A-Z (26 letras), sin la Ñ ni tildes.
- Convierte todo el texto a mayúsculas antes de procesar, así que no
  distingue mayúsculas de minúsculas en la salida.
- No es un cifrado seguro: al tener solo 26 claves posibles, cualquiera
  puede romperlo por fuerza bruta en segundos, como demuestra el propio
  programa.
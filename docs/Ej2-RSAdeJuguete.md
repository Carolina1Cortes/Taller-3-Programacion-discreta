# Papel de los números primos, el inverso modular y la congruencia en RSA

## Números primos

Los números primos son la base del algoritmo RSA. En el programa se
solicitan dos números primos `p` y `q`, cuya validez se comprueba
mediante la función `es_primo()`.

Su función es:

-   Calcular el módulo del sistema:

    `n = p × q`

-   Calcular la función de Euler:

    `φ(n) = (p - 1)(q - 1)`

La seguridad de RSA depende de que sea computacionalmente difícil
factorizar un número grande `n` en sus dos factores primos originales
(`p` y `q`). Si estos pudieran obtenerse fácilmente, también sería
posible calcular la clave privada.

## Inverso modular

El inverso modular permite obtener la clave privada `d`. En el código,
la función `inverso_modular()` utiliza el algoritmo de Euclides
extendido (`euclides_ext()`) para encontrar un número `d` que satisfaga:

`e · d ≡ 1 (mod φ(n))`

Esta relación significa que `d` es el inverso multiplicativo de `e`
módulo `φ(n)`.

Para que el inverso exista, es obligatorio que:

`gcd(e, φ(n)) = 1`

Por esta razón, el programa verifica esta condición antes de calcular la
clave privada.

## Congruencia modular

La congruencia modular es el fundamento matemático de RSA. Todas las
operaciones de cifrado y descifrado se realizan módulo `n`.

El cifrado se calcula como:

`C ≡ M^e (mod n)`

y el descifrado como:

`M ≡ C^d (mod n)`

En el programa estas operaciones se implementan mediante la función
`pow()` de Python con tres argumentos, que realiza la exponenciación
modular de forma eficiente.

Gracias a las propiedades de las congruencias y a la elección adecuada
de `e` y `d`, el mensaje recuperado después del descifrado coincide con
el mensaje original, siempre que se utilicen claves válidas.

## Relación entre los tres conceptos

Los tres elementos trabajan de forma conjunta durante el proceso de RSA:

1.  Los números primos permiten construir `n` y calcular `φ(n)`.
2.  El inverso modular calcula la clave privada `d` a partir de `e` y
    `φ(n)`.
3.  Las congruencias modulares hacen posible que el cifrado y el
    descifrado funcionen correctamente mediante operaciones de
    exponenciación módulo `n`.

Sin cualquiera de estos tres componentes, el algoritmo RSA no podría
generar claves válidas ni garantizar la recuperación correcta del
mensaje original.

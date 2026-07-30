# Taller 3 - Programación Discreta

Taller de la asignatura Matemáticas Discretas I (Universidad Nacional de
Colombia), que aplica ideas del curso —criptografía, grafos, álgebra de
Boole, teoría de la información y computación cuántica básica— en
programas pequeños y verificables.

## Integrantes
- Linda Carolina Cortes Bustos
- Antonio Garay Pinzon

## Lenguaje usado
Python 3

## Dependencias

### Librerías estándar de Python
Estas librerías vienen incluidas con Python y no requieren instalación.
- tkinter
- json
- math
- random
- heapq
- collections (defaultdict, Counter)

### Librerías externas
Instalar la siguiente dependencia antes de ejecutar el proyecto:
```bash
pip install sympy
```

### Instalación en Debian/Ubuntu
Si tkinter no está instalado, ejecutar:
```bash
sudo apt update
sudo apt install python3-tk
```
Posteriormente instalar la librería externa:
```bash
pip install sympy
```

## Cómo ejecutar
Cada ejercicio está en su propio archivo dentro de `src/`, organizado
por bloque temático. Para ejecutar uno, parado en la raíz del repositorio:

```bash
python src/cripto/CifradoCesar.py
python src/cripto/MPC.py
python src/grafos/dijkstra.py
python src/grafos/cierre_estacion.py
python src/boole/TablasVerdad.py
python src/boole/shannon.py
```

Las pruebas están en `tests/`. Para correrlas, parado dentro de `tests/`:
```bash
python PruebaEj1.py
python PruebaEj3.py
python PruebaEj5.py
python PruebaEj7.py
python PruebaEj9.py
```

## Estructura del repositorio
```text
├── src/
│ ├── cripto/ # Ejercicios 1, 2, 3
│ ├── grafos/ # Ejercicios 4, 5, 6
│ ├── boole/ # Ejercicios 7, 8, 9
│ └── cuantica/ # Ejercicio 10
├── tests/ # Pruebas de cada ejercicio
├── docs/ # Documentación matemática de cada ejercicio
└── README.md
```

## Uso de herramientas de IA

Se utilizó IA (Claude, de Anthropic) como apoyo para resolver dudas
puntuales durante el desarrollo:
- Explicación de conceptos matemáticos antes de programarlos (por
  ejemplo, cómo funciona el secret sharing en el ejercicio de MPC).
- Aclaración de errores de sintaxis y de lógica en el código (por
  ejemplo, el manejo de `__name__ == "__main__"`, o por qué una
  variable dentro de un `for` no se reiniciaba entre iteraciones).
- Sugerencias sobre buenas prácticas de manejo de errores
  (`try/except`) y estructura de pruebas.

Todo el código fue escrito, ejecutado y verificado por el propio
estudiante. La IA no generó el código final por sí sola: se usó como
apoyo para entender el problema y detectar errores propios, de la
misma forma en que se consultarían apuntes o documentación oficial.

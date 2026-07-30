import math
from collections import Counter


def calcular_frecuencias(texto):
    #Cuenta cuántas veces aparece cada símbolo en el texto.
    return dict(Counter(texto))


def calcular_probabilidades(texto):
    #Convierte las frecuencias en probabilidades (frecuencia / total).
    frecuencias = calcular_frecuencias(texto)
    total = len(texto)
    return {simbolo: frec / total for simbolo, frec in frecuencias.items()}


def entropia(texto):
    #Calcula H = -sum(p_i * log2(p_i)) sobre todos los símbolos del texto.
    if len(texto) == 0:
        return 0.0
    probabilidades = calcular_probabilidades(texto)
    return -sum(p * math.log2(p) for p in probabilidades.values())


def comparar_textos(texto1, texto2):
    #Calcula la entropía de dos textos y dice cuál es más incierto/variado.
    h1 = entropia(texto1)
    h2 = entropia(texto2)

    print(f"Texto 1: '{texto1}' -> entropía = {h1:.4f} bits/símbolo")
    print(f"Texto 2: '{texto2}' -> entropía = {h2:.4f} bits/símbolo")

    if h1 > h2:
        print("El texto 1 tiene mayor entropía (es más variado/impredecible).")
    elif h2 > h1:
        print("El texto 2 tiene mayor entropía (es más variado/impredecible).")
    else:
        print("Ambos textos tienen la misma entropía.")

    return h1, h2


if __name__ == "__main__":
    # Prueba 1: texto muy repetitivo (poca incertidumbre)
    texto_repetitivo = "AAAAAAAAAA"
    # Prueba 2: texto variado (símbolos distintos en proporciones parecidas)
    texto_variado = "ABCDABCDABCD"

    print("--- Frecuencias y probabilidades del texto variado ---")
    print("Frecuencias:", calcular_frecuencias(texto_variado))
    print("Probabilidades:", calcular_probabilidades(texto_variado))

    print("\n--- Comparación de entropía ---")
    comparar_textos(texto_repetitivo, texto_variado)
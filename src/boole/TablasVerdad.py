from itertools import product
import string

# Expresiones con 1 variable (extra, para mostrar que la solución generaliza)
expre1 = lambda A: not A

# Expresiones con 2 variables (extra)
expre2 = lambda A, B: A ^ B

# Expresiones con 3 variables 
expre3 = lambda A,B,C: (A and B) or (not C)
expre4 = lambda A,B,C: (A or B) and ((not A) or C)
expre5 = lambda A,B,C: (A ^ B) and C
# NAND:
expre6 = lambda A, B, C: not (A and B)
# XOR triple:
expre7 = lambda A, B, C: (A ^ B) ^ C   

#Expresiones con 4 variables 
expre8 = lambda A, B, C, D: (A and B) or (C and not D)
expre9 = lambda A, B, C, D: (A ^ B) and (C ^ D)
expre10 = lambda A, B, C, D: (A or B) and (not C or D) and (A ^ D)

# Diccionario para EJECUTAR: nombre -> función real
expresiones_disponibles = {
    "expre1": expre1, "expre2": expre2, "expre3": expre3,
    "expre4": expre4, "expre5": expre5, "expre6": expre6,
    "expre7": expre7, "expre8": expre8, "expre9": expre9,
    "expre10": expre10,
}


def tabla_de_verdad(expresion, num_variables):
    # Genera nombres para las columnas: A, B, C, etc.
    nombres_vars = list(string.ascii_uppercase[:num_variables])
    
    # Imprimir encabezado
    encabezado = " | ".join(nombres_vars) + " | Resultado"
    print(encabezado)
    print("-" * len(encabezado))
    
    # Imprimir cada fila
    for combinacion in product([0, 1], repeat=num_variables):
        resultado = bool(expresion(*combinacion))
        
        # Formateamos la combinación para que quede '0 | 1' en lugar de '(0, 1)'
        valores = " | ".join(map(str, combinacion))
        
        # Centramos o alineamos según el ancho de los encabezados
        print(f"{valores} | {resultado}")


def evaluar_entrada(expresion, *valores):
    resultado = bool(expresion(*valores))
    print(f'Entrada {valores} -> Resultado {resultado}')
    return resultado

# Diccionario para MOSTRAR: nombre -> descripción en notación matemática
descripciones = {
    "expre1": "¬A  [1 variable]",
    "expre2": "A⊕B  [2 variables]",
    "expre3": "(A∧B)∨¬C",
    "expre4": "(A∨B)∧(¬A∨C)",
    "expre5": "(A⊕B)∧C",
    "expre6": "¬(A∧B)  [NAND]",
    "expre7": "(A⊕B)⊕C  [XOR triple]",
    "expre8": "(A∧B)∨(C∧¬D)",
    "expre9": "(A⊕B)∧(C⊕D)",
    "expre10": "(A∨B)∧(¬C∨D)∧(A⊕D)",
}

# Diccionario que EVITA preguntarle al usuario el número de variables:
num_variables_por_expresion = {
    "expre1": 1, "expre2": 2, "expre3": 3, "expre4": 3, "expre5": 3,
    "expre6": 3, "expre7": 3, "expre8": 4,
    "expre9": 4, "expre10": 4,
}

def elegir_expresion():
    """ Muestra el menú de expresiones disponibles y pide al usuario un nombre.
    Repite la pregunta hasta que el nombre exista en el diccionario,
    evitando así que un nombre inválido (ej. 'expre99') rompa el programa."""

    print("Expresiones disponibles:")
    for nombre, descripcion in descripciones.items():
        print(f"  {nombre}: {descripcion}")

    while True:
        nombre = input("Ingresa la expresión (expre1, expre2, ...): ").strip()
        if nombre in expresiones_disponibles:
            return nombre
        print(f"'{nombre}' no es una expresión válida. Intenta de nuevo.\n")

def pedir_entero(mensaje):
    """Pide un número entero y repite la pregunta si el usuario escribe
    algo que no se puede convertir (ej. 'tres' en vez de 3)."""
    while True:
        texto = input(mensaje)
        try:
            return int(texto)
        except ValueError:
            print(f"'{texto}' no es un número válido. Intenta de nuevo.\n")

if __name__ == "__main__":
    print('-----------------------MENU-----------------------')
    print("1. Ver la tabla de verdad de una expresion logica.")
    print("2. Evaluar la expresion de una entrada.")
    print('----------------------------------------------')

    opcion = pedir_entero("Ingresa una de las opciones (1 o 2): ")

    if opcion == 1:
        nombre = elegir_expresion()
        num_variables = num_variables_por_expresion[nombre]  # ya no se pregunta, se sabe
        tabla_de_verdad(expresiones_disponibles[nombre], num_variables)

    elif opcion == 2:
        nombre = elegir_expresion()
        expresion = expresiones_disponibles[nombre]
        num_variables = num_variables_por_expresion[nombre]

        # Repetir hasta que la cantidad de valores coincida con la expresión elegida
        while True:
            texto_valores = input(f"Ingresa {num_variables} valores separados por coma (ej: 1,0,1): ")
            try:
                valores = [int(v) for v in texto_valores.split(",")]
            except ValueError:
                print("Todos los valores deben ser números (0 o 1). Intenta de nuevo.\n")
                continue

            if len(valores) != num_variables:
                print(f"Esta expresión necesita exactamente {num_variables} valores, "
                    f"pero ingresaste {len(valores)}. Intenta de nuevo.\n")
                continue
            
            if not all(v in (0, 1) for v in valores):
                print("Cada valor debe ser 0 o 1 (valores booleanos). Intenta de nuevo.\n")
                continue
            break

        evaluar_entrada(expresion, *valores)

    else:
        print("Opción inválida. Debe ser 1 o 2.")
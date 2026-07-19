def cifrar(texto, k):
    resultado = ""
    # Estandarizar el texto a mayúsculas para manejar un único rango ASCII
    texto = texto.upper()

    for caracter in texto:
    # Procesar únicamente caracteres alfabéticos (A-Z)
        if caracter.isalpha():
            # Mapear el carácter ASCII al rango numérico [0, 25] (A=0, B=1, ...)
            posicion = ord(caracter) - ord('A')
            # Aplicar desplazamiento César empleando aritmética modular de base 26
            nueva_posicion = (posicion + k) % 26
            # Convertir el nuevo índice numérico de regreso a su carácter ASCII
            nueva_letra = chr(nueva_posicion + ord('A'))
            resultado += nueva_letra
        else:
            # Mantener intactos espacios, números y signos de puntuación
            resultado += caracter

    return resultado


def descifrar(texto, k):
    resultado = ""
    texto = texto.upper()

    for caracter in texto:
        if caracter.isalpha():
            posicion = ord(caracter) - ord('A')
            # Deshacer el desplazamiento restando la clave bajo módulo 26
            nueva_posicion = (posicion - k) % 26
            nueva_letra = chr(nueva_posicion + ord('A'))
            resultado += nueva_letra
        else:
            resultado += caracter

    return resultado


def fuerzabruta(texto):
    texto = texto.upper()
    # Evaluar todo el espacio de claves posible (Z_26)
    for i in range(0,26):
        resultado = ""
        for caracter in texto:
        #Identificar si es una letra del abecedario
            if caracter.isalpha():
                posicion = ord(caracter) - ord('A')
                # Probar descifrado asumiendo 'i' como la clave actual
                nueva_posicion = (posicion - i) % 26
                nueva_letra = chr(nueva_posicion + ord('A'))
                resultado += nueva_letra
            else:
                resultado += caracter
        # Imprimir en consola el texto obtenido para la inspección visual de la clave correcta        
        print(f"k={i}: {resultado}")
    return

# Punto de entrada principal para la ejecución interactiva del script
if __name__ == "__main__":
    # Captura de datos proporcionados por el usuario
    texto = input("Ingresa el texto: ")
    k = int(input("Ingresa el desplazamiento k: "))
    # Demostración en consola del flujo completo del sistema
    print(cifrar(texto, k))                # Muestra el texto cifrado resultante
    print(descifrar(cifrar(texto, k), k))  # Verifica la reversibilidad (recupera el texto original)
    fuerzabruta(cifrar(texto, k))          # Ejecuta el análisis sobre el criptograma

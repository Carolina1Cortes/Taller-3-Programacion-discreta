def cifrar(texto, k):
    resultado = ""
    #Convertir toda la cadena a mayuscula
    texto = texto.upper()

    for caracter in texto:
    #Identificar si es una letra del abecedario
        if caracter.isalpha():
            posicion = ord(caracter) - ord('A')
            nueva_posicion = (posicion + k) % 26
            nueva_letra = chr(nueva_posicion + ord('A'))
            resultado += nueva_letra
        else:
            resultado += caracter

    return resultado


def descifrar(texto, k):
    resultado = ""
    #Convertir toda la cadena a mayuscula
    texto = texto.upper()

    for caracter in texto:
    #Identificar si es una letra del abecedario
        if caracter.isalpha():
            posicion = ord(caracter) - ord('A')
            nueva_posicion = (posicion - k) % 26
            nueva_letra = chr(nueva_posicion + ord('A'))
            resultado += nueva_letra
        else:
            resultado += caracter

    return resultado


def fuerzabruta(texto):
    #Convertir toda la cadena a mayuscula
    texto = texto.upper()

    for i in range(0,26):
        resultado = ""
        for caracter in texto:
        #Identificar si es una letra del abecedario
            if caracter.isalpha():
                posicion = ord(caracter) - ord('A')
                nueva_posicion = (posicion - i) % 26
                nueva_letra = chr(nueva_posicion + ord('A'))
                resultado += nueva_letra
            else:
                resultado += caracter
        print(f"k={i}: {resultado}")
    return


if __name__ == "__main__":
    texto = input("Ingresa el texto: ")
    k = int(input("Ingresa el desplazamiento k: "))
    print(cifrar(texto, k))
    print(descifrar(cifrar(texto, k), k))
    fuerzabruta(cifrar(texto, k))

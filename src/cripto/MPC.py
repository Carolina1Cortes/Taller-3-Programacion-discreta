from random import *


def distribuir_nota(nota,M):
    s1 = randint(0, M-1) 
    s2 = randint(0, M-1)
    s3 = (nota - s1 - s2) % M
    return (s1,s2,s3) 

    

def simular_servidores(notas, M):
    servidor1 = []
    servidor2 = []
    servidor3 = []

    # Validar todas las notas primero
    if len(notas) == 0:
        print("La lista de notas no puede estar vacía")
        return None
    
    for n in notas:
        if not (0 <= n <= 50):
            print("Por favor ingrese valores entre 0 y 50")
            return None   # <- se detiene aquí, sin seguir al ciclo

    # Reparte cada nota de forma independiente y distribuye sus partes
    for n in notas:
            s1, s2, s3 = distribuir_nota(n,M)
            servidor1.append(s1)
            servidor2.append(s2)
            servidor3.append(s3)
    return servidor1, servidor2, servidor3

def recontruir_suma_promedio(notas, M):
    suma = 0
    servidores = simular_servidores(notas, M)
    if servidores is None:   # <- si hubo un error, no sigas
        return 
    
    for s in range(len(servidores)):
        suma += sum(servidores[s])

    suma_final = suma % M
    promedio = suma_final/len(notas)

    #print(f"Suma total = {suma_final}, Promedio = {promedio}")
    return suma_final, promedio

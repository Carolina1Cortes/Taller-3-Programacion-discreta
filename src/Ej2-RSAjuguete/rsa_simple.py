import math

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def euclides_ext(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = euclides_ext(b, a % b)
    return g, y1, x1 - (a // b) * y1

def inverso_modular(e, phi):
    g, x, _ = euclides_ext(e, phi)
    if g != 1:
        return None
    return x % phi

def calcular_rsa(p, q, e, m):
    n = p * q
    phi = (p - 1) * (q - 1)
    d = inverso_modular(e, phi)
    if d is None:
        return None
    c = pow(m, e, n)
    m2 = pow(c, d, n)
    return {"n": n, "phi": phi, "d": d, "c": c, "m": m2}

def pedir_entero(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Valor invalido.")

def modo_libre():
    p = pedir_entero("p: ")
    q = pedir_entero("q: ")
    if not es_primo(p) or not es_primo(q):
        print("p y q deben ser primos.")
        return
    e = pedir_entero("e: ")
    m = pedir_entero("M: ")
    phi = (p - 1) * (q - 1)
    if math.gcd(e, phi) != 1:
        print(f"e invalido, gcd(e, phi)={math.gcd(e, phi)} != 1")
        return
    r = calcular_rsa(p, q, e, m)
    print(f"n={r['n']} phi={r['phi']} d={r['d']} C={r['c']} M_desc={r['m']}")

def casos_obligatorios():
    casos = [
        {"p": 61, "q": 53, "e": 17, "m": 65},
    ]
    while True:
        print("\n--- Casos obligatorios ---")
        for i, c in enumerate(casos, 1):
            print(f"{i}. p={c['p']} q={c['q']} e={c['e']} M={c['m']}")
        print("0. Volver")
        op = input("Opcion: ")
        if op == "0":
            return
        try:
            idx = int(op) - 1
            c = casos[idx]
        except (ValueError, IndexError):
            print("Opcion invalida.")
            continue
        r = calcular_rsa(c["p"], c["q"], c["e"], c["m"])
        print(f"n={r['n']} phi={r['phi']} d={r['d']} C={r['c']} M_desc={r['m']}")

def menu():
    while True:
        print("\n=== RSA Taller ===")
        print("1. Casos obligatorios")
        print("2. Modo libre")
        print("0. Salir")
        op = input("Opcion: ")
        if op == "1":
            casos_obligatorios()
        elif op == "2":
            modo_libre()
        elif op == "0":
            break
        else:
            print("Opcion invalida.")

if __name__ == "__main__":
    menu()
import random

def cumpleaños(m):
    dias = set()
    for _ in range(m):
        cumple = random.randint(1, 365)
        if cumple in dias:
            return True  # al menos dos personas con el mismo cumpleaños
        dias.add(cumple)
    return False  # todos con cumpleaños distintos

def simular(n_simulaciones, m):
    victorias = 0
    derrotas = 0
    for _ in range(n_simulaciones):
        if cumpleaños(m):
            victorias += 1
        else:
            derrotas += 1
    return victorias, derrotas

valores_m = [10, 20, 30, 40, 50] #numero de personas a probar
valores_n = [1000, 10000, 100000] #veces que repito la simulacion

for n in valores_n:
    print(f"\nSimulaciones: {n}")
    for m in valores_m:
        victorias, derrotas = simular(n, m)
        print(f"m = {m}: Victorias = {victorias}, Derrotas = {derrotas}")

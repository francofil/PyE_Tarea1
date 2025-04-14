#imports
import random

#Funcion Monty Hall, con prinst en cada paso para entender la funcion
def montyHallWhitPrints(cambio: bool) -> bool:
    puertas = [1, 2, 3]
    eleccion = random.choice(puertas)
    auto = random.choice(puertas) 
    opcion_presentador = []
    print(f"Opciones de puertas:{puertas}")
    print(f"Puerta elegida incialmente: {eleccion}")
    print(f"El auto se encuentra en la puerta: {auto}")
    
    if (eleccion == auto):
        opciones_presentador = [puerta for puerta in puertas if puerta != eleccion]
        print(f"Opciones para que monty abra: {opciones_presentador}")
    else:
        opciones_presentador = [p for p in puertas if p != eleccion and p != auto]
        print(f"Opciones para que monty abra: {opciones_presentador}")

    opcion_presentador = random.choice(opciones_presentador)
    print(f"Monty abre la puerta: {opcion_presentador}")
    puertas.remove(opcion_presentador)
    print(f"Opciones puertas pre segunda eleccion: {puertas}")

    if cambio:
        eleccion = [p for p in puertas if p != eleccion]
        print(f"El participante elige cambiar a la puerta: {eleccion}")
        print(f"El auto se encuentra en la puerta: {auto}")
    else:
        print(f"El participante elige mantener la puerta: {eleccion}")
        print(f"El auto se encuentra en la puerta: {auto}")

    if auto in eleccion:
        print("El participante ha ganado el auto!")
        return True
    else:
        print("El participante ha perdido el auto!")
        return False

#Funcion Monty Hall, sin prints para correr el experimento
def montyHall(cambio: bool) -> bool:
    puertas = [1, 2, 3]
    eleccion = random.choice(puertas)
    auto = random.choice(puertas)

    if eleccion == auto:
        opciones_presentador = [p for p in puertas if p != eleccion]
    else:
        opciones_presentador = [p for p in puertas if p != eleccion and p != auto]

    opcion_presentador = random.choice(opciones_presentador)
    puertas.remove(opcion_presentador)

    if cambio:
        eleccion = [p for p in puertas if p != eleccion][0]

    return eleccion == auto

def contadorEstrategia(cambio: bool, intentos: int) -> int:
    contadorGana = 0
    for i in range(intentos):
        if montyHall(cambio):
            contadorGana += 1
    return contadorGana


cant = 100000
ganadas_cambio = contadorEstrategia(True, cant)
ganadas_no_cambio = contadorEstrategia(False, cant)

print("\nResultados de la estrategia de cambiar:")
print(f"Gano {ganadas_cambio} veces en {cant} intentos ({ganadas_cambio / cant:.5f})")

print("\nResultados de la estrategia de NO cambiar:")
print(f"Gano {ganadas_no_cambio} veces en {cant} intentos ({ganadas_no_cambio / cant:.5f})")





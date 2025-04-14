import random


# 1) Pregunta 1

# Informaciom del problema
prob_enfermedad = 1 / 10000  # Probabilidad de tener la enfermedad
prob_pos_si_enfermo = 0.99  # Probabilidad de que el test sea positivo dado que la persona tiene la enfermedad
prob_pos_si_no_enfermo = 0.02  # Probabilidad de que el test sea positivo dado que la persona no tiene la enfermedad


def simulacion(num_personas):
    positivos = 0
    enfermos_y_positivos = 0

    for _ in range(num_personas):
        tiene_enfermedad = random.random() < prob_enfermedad
        
        if tiene_enfermedad:
            test_positivo = random.random() < prob_pos_si_enfermo
        else:
            test_positivo = random.random() < prob_pos_si_no_enfermo
        
        if test_positivo:
            positivos += 1
            if tiene_enfermedad:
                enfermos_y_positivos += 1

    if positivos > 0:
        probabilidad_estimacion = enfermos_y_positivos / positivos
    else:
        probabilidad_estimacion = 0

    return probabilidad_estimacion

# Número de personas simuladas
num_personas = 100000
probabilidad_estimacion = simulacion(num_personas)
print(f"Probabilidad estimada de tener la enfermedad dado que el test fue positivo: {probabilidad_estimacion:.5f}")


# Pregunta 2 SE ENTREGA EN FORMATO DE IMAGEN

# Pregunta 3: 

# No, el resultado no es completamente intuitivo.

# Aunque el test es bastante preciso (99% de aciertos cuando la persona tiene la enfermedad), 
# la probabilidad de que una persona realmente tenga la enfermedad dado que el test fue positivo sigue siendo baja. 
# Esto es porque la enfermedad es rara (solo 1 de cada 10,000 personas la tiene) y hay falsos positivos (el 2% de las personas sanas da positivo).

# Así que, aunque el test da un positivo, la mayoría de los positivos provienen de personas sanas debido a los falsos positivos. 
# Esto hace que la probabilidad de que realmente tenga la enfermedad siga siendo baja, a pesar del test positivo.

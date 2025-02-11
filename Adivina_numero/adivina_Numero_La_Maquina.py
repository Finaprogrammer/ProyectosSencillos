import random


def adivina_el_numero_maquina(limite_inferior, limite_superior):
    print("===============================================")
    print("¡Bienvenido al juego de adivinar el número!")
    print("===============================================")
    print(f"selecciona un numero entre 1 y {limite_superior} para que el pc intente adivinarlo")

    limite_inferior = 1
    respuesta=""
    while respuesta != "c":
        if limite_inferior != limite_superior: # si el limite inferior es igual al limite superior, significa que el numero lo hemos adivinado
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior
        respuesta = input(f"Mi predicción es {prediccion}. ¿Es correcta, mayor o menor? (c/m/n): ").lower().strip()
        if respuesta == "m":
            limite_inferior = prediccion + 1
        elif respuesta == "n":
            limite_superior = prediccion - 1
    print(f"¡Sí! He adivinado tu número {prediccion}.")

if __name__ == "__main__":
    adivina_el_numero_maquina(1,10)

    
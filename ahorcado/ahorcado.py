import random

def elegir_palabra():
    palabras = ["python", "programacion", "ahorcado", "desarrollo", "codigo"]
    return random.choice(palabras)

def mostrar_progreso(palabra, letras_adivinadas):
    return " ".join([letra if letra in letras_adivinadas else "_" for letra in palabra])

def ahorcado():
    print("¡Bienvenido al juego del Ahorcado!")
    palabra = elegir_palabra()
    letras_adivinadas = set()
    intentos_restantes = 6

    while intentos_restantes > 0:
        print("\nPalabra:", mostrar_progreso(palabra, letras_adivinadas))
        print(f"Intentos restantes: {intentos_restantes}")
        letra = input("Adivina una letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresa una sola letra válida.")
            continue

        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra.")
            continue

        letras_adivinadas.add(letra)

        if letra in palabra:
            print("¡Bien hecho! La letra está en la palabra.")
            if all(letra in letras_adivinadas for letra in palabra):
                print(f"¡Felicidades! Has adivinado la palabra: {palabra}")
                break
        else:
            print("La letra no está en la palabra.")
            intentos_restantes -= 1

    if intentos_restantes == 0:
        print(f"¡Has perdido! La palabra era: {palabra}")

if __name__ == "__main__":
    ahorcado()
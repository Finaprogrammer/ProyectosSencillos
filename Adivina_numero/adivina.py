import random

def adivina_el_numero(x, numero):
    print("===============================================")
    print("¡Bienvenido al juego de adivinar el número!")
    print("===============================================")
    print("Tu meta es adivinar el número que estoy pensando")

    if x == numero:
        return "¡Felicidades! Has adivinado el número."
    elif x < numero:
        return "El número es mayor que " + str(x)
    else:
        return "El número es menor que " + str(x)
    
if __name__ == "__main__":
    numero = random.randint(1, 100)
    while True:
        try:
            user_input = int(input("Ingresa un número: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue
        
        resultado = adivina_el_numero(user_input, numero)
        print(resultado)
        
        if user_input == numero:
            opcion = input("¿Quieres jugar de nuevo? (s/n): ").lower().strip()
            if opcion != "s":
                break
            else:
                numero = random.randint(1, 100)
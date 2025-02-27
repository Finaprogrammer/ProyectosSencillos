import random

def main():
    print("¡Bienvenido a Piedra, Papel o Tijera!")
    print("-------------------------------------")
    
    options = ["piedra", "papel", "tijera"]
    user_score = 0
    computer_score = 0
    
    while True:
        print(f"\nPuntuación: Usuario {user_score} - {computer_score} Computadora")
        
        # Get user choice
        user_choice = input("\nElige piedra, papel o tijera (o 'salir' para terminar): ").lower()
        
        if user_choice == 'salir':
            break
            
        if user_choice not in options:
            print("Opción no válida. Inténtalo de nuevo.")
            continue
            
        # Computer chooses randomly
        computer_choice = random.choice(options)
        
        print(f"Tu elección: {user_choice}")
        print(f"Computadora elige: {computer_choice}")
        
        # Determine the winner
        if user_choice == computer_choice:
            print("¡Empate!")
        elif (user_choice == "piedra" and computer_choice == "tijera") or \
             (user_choice == "papel" and computer_choice == "piedra") or \
             (user_choice == "tijera" and computer_choice == "papel"):
            print("¡Ganaste!")
            user_score += 1
        else:
            print("¡Perdiste!")
            computer_score += 1
    
    print("\n--- Resultado Final ---")
    print(f"Puntuación final: Usuario {user_score} - {computer_score} Computadora")
    
    if user_score > computer_score:
        print("¡Felicidades! Has ganado el juego.")
    elif user_score < computer_score:
        print("Has perdido el juego. ¡Mejor suerte la próxima vez!")
    else:
        print("El juego ha terminado en empate.")
    
if __name__ == "__main__":
    main()
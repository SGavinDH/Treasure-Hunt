import random

def print_intro():
    print("Welcome to Treasure Hunt!")
    print("You're on a 5x5 grid. Find the hidden treasure!")
    print("You have 10 attempts. Good luck!\n")

def get_coordinates():
    while True:
        try:
            x = int(input("Enter X (1-5): "))
            y = int(input("Enter Y (1-5): "))
            if 1 <= x <= 5 and 1 <= y <= 5:
                return x, y
            else:
                print("Coordinates must be between 1 and 5.")
        except ValueError:
            print("Please enter valid numbers.")

def play_game():
    treasure_x = random.randint(1, 5)
    treasure_y = random.randint(1, 5)
    attempts = 10

    print_intro()

    while attempts > 0:
        print(f"Attempts left: {attempts}")
        x, y = get_coordinates()

        if x == treasure_x and y == treasure_y:
            print("🎉 You found the treasure! You win!")
            return
        else:
            hint_x = "left" if x > treasure_x else "right"
            hint_y = "up" if y > treasure_y else "down"
            print(f"No treasure here. Try going {hint_x} and {hint_y}.\n")
            attempts -= 1

    print("💀 Game over! You ran out of attempts.")
    print(f"The treasure was at ({treasure_x}, {treasure_y}).")

if __name__ == "__main__":
    play_game()
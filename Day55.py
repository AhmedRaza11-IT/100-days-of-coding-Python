# Snake Water gun

import random

def check_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "snake" and computer_choice == "water") or \
         (user_choice == "water" and computer_choice == "gun") or \
         (user_choice == "gun" and computer_choice == "snake"):
        return "You win!"
    else:
        return "Computer wins!"

def snake_water_gun_game():
    choices = ["snake", "water", "gun"]
    user_choice = input("Enter your choice (snake, water, gun): ").lower()

    if user_choice not in choices:
        print("Invalid choice! Please choose snake, water, or gun.")
        return

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    result = check_winner(user_choice, computer_choice)
    print(result)

# Run the game
if __name__ == "__main__":
    snake_water_gun_game()

import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

# Function to get the computer's choice
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

# Main game loop
def play_game():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        replay = input("Do you want to play again? (yes/no): ").lower()
        if replay != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()

import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"

def print_choices(user_choice, computer_choice):
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

def print_result(result):
    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win!")
    elif result == "computer":
        print("Computer wins!")

def print_scores(user_score, computer_score):
    print(f"Scores - You: {user_score}, Computer: {computer_score}")

def play_game():
    choices = ['rock', 'paper', 'scissors']
    user_score = 0
    computer_score = 0
    
    while True:
        print("\nLet's play Rock-Paper-Scissors!")
        print("Enter your choice (rock, paper, scissors) or 'quit' to end the game:")
        user_choice = input().lower()
        
        if user_choice == 'quit':
            break
        elif user_choice not in choices:
            print("Invalid choice. Please choose again.")
            continue
        
        computer_choice = random.choice(choices)
        
        print_choices(user_choice, computer_choice)
        
        result = determine_winner(user_choice, computer_choice)
        print_result(result)
        
        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1
        
        print_scores(user_score, computer_score)
        
    print("\nThanks for playing!")

play_game()


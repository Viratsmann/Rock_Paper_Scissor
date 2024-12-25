import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissor"]

while True:
    user_input = input("Rock, paper, or scissor and q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_choice = random.randint(0, 2)
    computer_choice = options[random_choice]
    print(f"Computer chose {computer_choice}")

    if user_input == 'rock' and computer_choice == 'scissor':
        print("You won!")
        user_wins += 1

    elif user_input == 'paper' and computer_choice == 'rock':
        print("You won!")
        user_wins += 1

    elif user_input == 'scissor' and computer_choice == 'paper':
        print("You won!")
        user_wins += 1

    else:
        print("You lost")
        computer_wins += 1

print(f"You won {user_wins} times.")
print(f"Computer won {computer_wins} times.")
print('goodbye')
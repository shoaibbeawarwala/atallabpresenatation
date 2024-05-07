import random

# Guessing Game
def guessing_game():
    MAX_VALUE = 100
    random_number = random.randint(1, MAX_VALUE)
    guesses = 0

    while True:
        guess = int(input(f"Guess a number between 1 and {MAX_VALUE}: "))
        guesses += 1

        if guess == random_number:
            print(f"Congratulations! You guessed the number in {guesses} guesses.")
            break
        elif guess < random_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

# Fibonacci Sequence
def fibonacci_sequence():
    SEQUENCE_LENGTH = 20
    fibonacci_sequence = [0, 1]

    for i in range(2, SEQUENCE_LENGTH):
        next_number = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
        fibonacci_sequence.append(next_number)

    print("Fibonacci Sequence:")
    for number in fibonacci_sequence:
        print(number)

# Palindrome Checker
def is_palindrome(string):
    clean_string = string.replace(" ", "").lower()
    reversed_string = clean_string[::-1]
    return clean_string == reversed_string

def palindrome_checker():
    user_input = input("Enter a string to check if it's a palindrome: ")

    if is_palindrome(user_input):
        print(f"{user_input} is a palindrome!")
    else:
        print(f"{user_input} is not a palindrome.")

# Rock, Paper, Scissors
def get_computer_choice():
    CHOICES = ["rock", "paper", "scissors"]
    return random.choice(CHOICES)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def rock_paper_scissors():
    while True:
        user_choice = input("Choose rock, paper, or scissors (or 'q' to quit): ").lower()

        if user_choice == "q":
            break

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Try again.")
            continue

        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)

        print(f"You chose {user_choice}, and the computer chose {computer_choice}. {result}")

# Text-based Adventure Game
def showInstructions():
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
      use [item]
    ''')

def showStatus(currentRoom, inventory):
    print('---------------------------')
    print('You are in the ' + currentRoom['name'])
    print('You can go:')
    for direction in currentRoom['directions']:
        print('   ' + direction)
    print('Inventory:', ', '.join(inventory))
    if 'item' in currentRoom:
        print('You see a ' + currentRoom['item'])
    print("---------------------------")

def move(currentRoom, direction, rooms):
    if direction in currentRoom['directions']:
        newRoom = rooms[currentRoom['directions'][direction]]
        return newRoom
    else:
        print("You can't go that way!")
        return currentRoom

def get(currentRoom, inventory):
    if 'item' in currentRoom:
        item = currentRoom['item']
        inventory.append(item)
        print('You got the ' + item + '!')
        del currentRoom['item']
    else:
        print('There is nothing to get.')
    return inventory

def use(currentRoom, inventory, rooms):
    if 'use' in currentRoom and currentRoom['use'] in inventory:
        print(currentRoom['use_message'])
        if 'use_direction' in currentRoom:
            newRoom = rooms[currentRoom['directions'][currentRoom['use_direction']]]
            return newRoom
    else:
        print("You can't use anything here.")
    return currentRoom

def adventure_game():
    rooms = {
        'entrance': {'name': 'Entrance', 'directions': {'north': 'cave'}, 'item': 'torch'},
        'cave': {'name': 'Cave', 'directions': {'south': 'entrance', 'east': 'tunnel'}, 'use': 'torch', 'use_message': 'The torch lights up the dark cave.', 'use_direction': 'east'},
        'tunnel': {'name': 'Tunnel', 'directions': {'west': 'cave', 'north': 'treasure'}, 'item': 'key'},
        'treasure': {'name': 'Treasure Room', 'directions': {'south': 'tunnel'}, 'use': 'key', 'use_message': 'You unlocked the treasure chest!'}
    }

    inventory = []
    currentRoom = rooms['entrance']

    showInstructions()

    while True:
        showStatus(currentRoom, inventory)
        move_input = input('> ').lower().split()

        if move_input[0] == 'go':
            if len(move_input) > 1:
                direction = move_input[1]
                currentRoom = move(currentRoom, direction, rooms)
            else:
                print('Go where?')

        elif move_input[0] == 'get':
            if len(move_input) > 1:
                inventory = get(currentRoom, inventory)
            else:
                print('Get what?')

        elif move_input[0] == 'use':
            if len(move_input) > 1:
                currentRoom = use(currentRoom, inventory, rooms)
            else:
                print('Use what?')

        elif move_input[0] == 'quit':
            break

        else:
            print("I don't understand that command.")

# Main menu
while True:
    print("\nWelcome to the Python Programming Playground!")
    print("Please choose an option:")
    print("1. Guessing Game")
    print("2. Fibonacci Sequence")
    print("3. Palindrome Checker")
    print("4. Rock, Paper, Scissors")
    print("5. Text-based Adventure Game")
    print("6. Quit")

    choice = input("> ")

    if choice == "1":
        guessing_game()
    elif choice == "2":
        fibonacci_sequence()
    elif choice == "3":
        palindrome_checker()
    elif choice == "4":
        rock_paper_scissors()
    elif choice == "5":
        adventure_game()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
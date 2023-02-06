import random

def game():
    tries = 0
    number = random.randint(1, 20)

    print("Hello! What is your name?")
    name = input()

    print("Well, KBTU, I am thinking of a number between 1 and 20.")

    print("Take a guess.")
    guess = int(input())
    
    while guess != number:
        tries += 1
        print("Your guess is too low.")
        print("Take a guess.")
        
        guess = int(input())
    else:
        print("Good job," + name + "! You guessed my number in " + str(tries) + " guesses!")
        return

game()

# Importing a module
import random

# Defining a function
def greet(name):
    return f"Hello, {name}!"

# Function with control structure
def guess_number():
    secret = random.randint(1, 10)
    attempts = 3
    print("Guess a number between 1 and 10!")
    
    while attempts > 0:
        guess = int(input(f"You have {attempts} attempts left. Enter your guess: "))
        if guess == secret:
            return "You won!"
        elif guess < secret:
            print("Too low!")
        else:
            print("Too high!")
        attempts -= 1
    return f"Game over! The number was {secret}."

# Main execution
if __name__ == "__main__":
    # Using the greet function
    print(greet("Faizan"))
    
    # Using a for loop
    print("Counting to 5:")
    for i in range(1, 6):
        print(i)
    
    # Running the guessing game
    print("\nStarting number guessing game...")
    print(guess_number())
# run "python guess_number.py"
import random

def main():
    print("🎉 Welcome to the Number Guessing Game!")
    number = random.randint(1, 100)
    attempts = 0
    
    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1
        
        if guess < number:
            print("Too low! 📉")
        elif guess > number:
            print("Too high! 📈")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} tries!")
            break

if __name__ == "__main__":
    main()

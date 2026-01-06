import random

def number_guessing_game():
    """A simple number guessing game with difficulty levels"""
    print("=" * 50)
    print("Welcome to the Number Guessing Game!")
    print("=" * 50)
    
    # Choose difficulty
    print("\nSelect Difficulty:")
    print("1. Easy (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard (1-200, 5 attempts)")
    
    difficulty = input("\nEnter choice (1-3): ")
    
    if difficulty == '1':
        max_num, attempts = 50, 10
    elif difficulty == '2':
        max_num, attempts = 100, 7
    elif difficulty == '3':
        max_num, attempts = 200, 5
    else:
        print("Invalid choice! Defaulting to Medium.")
        max_num, attempts = 100, 7
    
    secret_number = random.randint(1, max_num)
    attempts_left = attempts
    
    print(f"\nI'm thinking of a number between 1 and {max_num}")
    print(f"You have {attempts} attempts to guess it!\n")
    
    while attempts_left > 0:
        try:
            guess = int(input(f"Attempt {attempts - attempts_left + 1}/{attempts} - Enter your guess: "))
            
            if guess < 1 or guess > max_num:
                print(f"Please enter a number between 1 and {max_num}!")
                continue
            
            if guess == secret_number:
                print(f"\n🎉 Congratulations! You guessed it in {attempts - attempts_left + 1} attempts!")
                print(f"The number was {secret_number}")
                break
            elif guess < secret_number:
                print("📈 Too low! Try a higher number.")
            else:
                print("📉 Too high! Try a lower number.")
            
            attempts_left -= 1
            
            if attempts_left > 0:
                print(f"Attempts remaining: {attempts_left}\n")
            else:
                print(f"\n😔 Game Over! The number was {secret_number}")
                
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    # Play again option
    play_again = input("\nWould you like to play again? (yes/no): ")
    if play_again.lower() in ['yes', 'y']:
        number_guessing_game()
    else:
        print("Thanks for playing! Goodbye! 👋")

if __name__ == "__main__":
    number_guessing_game()

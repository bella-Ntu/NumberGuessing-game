import random

def guess_game():
    lower_bound = 1
    upper_bound = 100
    
    while True:
        secret_number = random.randint(lower_bound, upper_bound)
        attempts_allowed = 7
        attempts_used = 0
        won = False

        print(f"\n------ New Round: Guess a number between {lower_bound} and {upper_bound} ------")

        while attempts_used < attempts_allowed:
            user_input = input(f"Attempt {attempts_used + 1}/{attempts_allowed} - Enter your guess: ")

            try:
                guess = int(user_input)
            except ValueError:
                print("Invalid input! Please enter a whole number.")
                continue

            attempts_used += 1

            if guess < secret_number:
                print("Too Low!")
            elif guess > secret_number:
                print("Too High!")
            else:
                print(f"🎉🎉Congragulations! You got it right in {attempts_used} attempts.🎉🎉")
                won = True
                break

        if not won:
            print(f"Game Over🕹️🕹️! The correct number was {secret_number}.")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again == 'yes':
            upper_bound += 50  
        else:
            print("Thanks for playing!Hope we meet again next time")
            break

if __name__ == "__main__":
    guess_game()

                                                    #ALITUHA SHABELLA - 25/BSE/BU/R/0016

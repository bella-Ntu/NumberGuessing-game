import random

print('WELCOME TO THE NUMBER GUESSING GAME!')

while True:
    secret_Number = random.randint(1,100)
    attempts = 0

    print('''\nI've picked a Random Number between 1 & 100.
            Try to Guess it!     ''')
    
    while True:
        guess = int(input('Your Guess: '))
        attempts += 1

        if guess < secret_Number:
            print('Too low!')
        elif guess > secret_Number:
            print('Too high!')
        else:
            print(f'🎉🎉 Congragulations! You got it in {attempts} tries!🎉🎉')
            break

    again = input('\nDo u want to play again? [yes / exit]: ').lower()

    if again == 'exit':
        print('Thanks for playing. Goodbye👋👋')
        break
    elif again != 'yes':
        print("I'll take that as 'exit'. Goodbye!'")
    break
                                                #ALITUHA SHABELLA - 25/BSE/BU/R/0016
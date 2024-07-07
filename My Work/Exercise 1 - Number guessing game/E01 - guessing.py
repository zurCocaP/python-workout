import random

def guessing_game():
    number = random.randint(0, 100)

    while True:
        user_guess = int(input('What is your guess?: '))

        if user_guess == number:
            print(f'Right! The answer is {user_guess}')
            break

        if user_guess < number:
            print(f'Your guess of {user_guess} is too low.')
        else:
            print(f'Your guess of {user_guess} is too high')

# guessing_game()

def three_guesses():
    number = random.randint(0,100)
    attempts = 5

    for i in range(attempts):
        user_guess = int(input('What is your guess?: '))

        if user_guess == number:
            print(f'Right! The answer is {user_guess}')
            break

        if user_guess < number:
            print(f'Your guess of {user_guess} is too low.')
        else:
            print(f'Your guess of {user_guess} is too high')

        if i == attempts - 1:
            print(f'You didn\'t guess the number {number} in {attempts} attempts.')

three_guesses()
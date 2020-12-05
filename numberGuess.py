import random

random_number = random.randint(0, 100)

print('Welcome to the Guessing Game Challenge! \n\n'
      'The program will randomly pick an integer number between 1 and 100. \n'
      'The user must then guess what this number is in the least amount of \n'
      'guesses as possible. After each guess, the program will indicate how \n'
      'close or far the user\'s guess is from the actual number. \n')

# list to keep all of the guesses made
user_guesses = [0]

while True:
    guess = input('Enter a number between 1 and 100: ')

    # check that input is an integer
    try:
        is_guess_int = int(guess)
    except ValueError:
        print('Invalid input.')
        continue

    # check that input is between 1 and 100
    if int(guess) < 1 or int(guess) > 100:
        print("The number entered is out of bounds.")
        continue

    # if user guesses the correct number
    if int(guess) == random_number:
        print('You guessed it! The correct number was ' + str(random_number) + '!\n'
              'You took ' + str(len(user_guesses)) + ' guesses total.')
        break

    # first guess of game
    if user_guesses[0] == 0:
        if abs(int(guess) - random_number) <= 10:
            # guess is within 10 numbers from the actual number
            print('Your first guess is close to the actual number!')
            user_guesses[0] = int(guess)
            continue
        elif abs(int(guess) - random_number) > 10:
            # guess is further than 10 numbers away from actual number
            print('Your first guess is far from the actual number!')
            user_guesses[0] = int(guess)
            continue
    else:
        # every guesses after first
        user_guesses.append(int(guess))

        if abs(user_guesses[-2] - random_number) >= abs(int(guess) - random_number):
            # current guess is closer than previous guess
            print('Your next guess is closer!')
            continue
        elif abs(user_guesses[-2] - random_number) < abs(int(guess) - random_number):
            # current guess is further than previous guess
            print('Your next guess is further!')
            continue
    pass

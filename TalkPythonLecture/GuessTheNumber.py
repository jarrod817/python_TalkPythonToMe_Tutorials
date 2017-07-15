import random
print('---------------------------- \n     Guess that number \n----------------------------')

number = random.randint(0, 100)
guess = -1
while guess != number:
    guess = int(input('Guess a number between 0 and 100: '))
    if guess < number:
        print('Sorry, {} is less than the number'.format(guess))
    elif guess > number:
        print('Sorry, {} is larger than the number'.format(guess))
    else:
        print('Congradulations! You got it! The number is {}'.format(guess))

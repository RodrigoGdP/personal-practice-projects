import random
base = 1
ceiling = 100
guesses = 10
num = random.randint(base, ceiling)
print(f'I am thinking of a number between {base} and {ceiling}.\nYou have {guesses} guesses.')
for guesses_taken in range (10):
    guess = int(input())
    guesses -= 1
    if guess < num:
        print (f'Your guess is too low, try again.\nGuesses left: {guesses}')
    elif guess > num:
        print (f'Your guess is too high, try again.\nGuesses left: {guesses} ')
    else:
        break
if guess == num:
    print(f'Congratulations, you guessed my number in {guesses_taken} guesses.')
else:
    print(f'You ran out of guesses! My number was {num}.')
import random
wins = 0
losses = 0
ties = 0
a = 0
guess = ''
print("It's Rock, Paper, Scissors!")
while True:
    print('Your move. Choose ROCK (r), PAPER (p), SCISSORS (s) or QUIT (q)')
    guess = input()
    a = random.randint(1,3)
    if guess == 'r' or guess == 'p' or guess == 's' or guess == 'q':
        if a == 1:
            a = 'r'
        elif a == 2:
            a = 'p'
        elif a == 3:
            a = 's'

        if guess == 'r' and a == 'r':
            print("Your ROCK vs the computer's ROCK. It's a tie!")
            ties += 1
        elif guess == 'r' and a == 'p':
            print("Your ROCK vs the computer's PAPER. You lose!")
            losses += 1
        elif guess == 'r' and a == 's':
            print("Your ROCK vs the computer's SCISSORS. You win!")
            wins += 1
        elif guess == 'p' and a == 'r':
            print("Your PAPER vs the computer's ROCK. You win!")
            wins += 1
        elif guess == 'p' and a == 'p':
            print("Your PAPER vs the computer's PAPER. It's a tie!")
            ties += 1
        elif guess == 'p' and a == 's':
            print("Your PAPER vs the computer's SCISSORS. You lose!")
            losses += 1
        elif guess == 's' and a == 'r':
            print("Your SCISSORS vs the computer's ROCK. You lose!")
            losses += 1
        elif guess == 's' and a == 'p':
            print("Your SCISSORS vs the computer's PAPER. You win!")
            wins += 1
        elif guess == 's' and a == 's':
            print("Your SCISSORS vs the computer's SCISSORS. It's a tie!")
            ties += 1
        elif guess == 'q':
            break
        print(f'Wins: {wins}; Losses: {losses}; Ties: {ties}')
    else:
        print('Invalid command...')

print('You quit.')


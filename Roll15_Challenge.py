# Copy and paste this code a Python IDE. It's ready to run.
import random


def roll6():
    a = (random.randint(1, 6))
    return a


# Define function roll15()
def roll15():
    # Get random numbers from 1 to 3
    b1_3 = roll6()
    while b1_3 > 3:
        b1_3 = roll6()

    # Get random numbers from 4 to 9
    b4_9 = roll6() + 3

    # Get random numbers from 10 to 15
    b10_15 = roll6() + 9

    # List with the three variables
    c = [b1_3, b4_9, b10_15]

    # Get a random number from 1 to 3
    d = roll6()
    while d > 3:
        d = roll6()

    # Choose one element from the list and print it based on variable d
    if d == 1:
        print(c[0])
    elif d == 2:
        print(c[1])
    elif d == 3:
        print(c[2])


# Call the function
 roll15()

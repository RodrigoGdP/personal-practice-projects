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

    # Get random numbers from 4 to 6
    b4_6 = roll6()
    while b4_6 < 4:
        b4_6 = roll6()

    # Get random numbers from 7 to 9
    b7_9 = roll6() + 3
    while b7_9 < 7:
        b7_9 = roll6() + 3

    # Get random numbers from 10 to 12
    b10_12 = roll6() + 9
    while b10_12 > 12:
        b10_12 = roll6() + 9

    # Get random numbers from 13 to 15
    b13_15 = roll6() + 9
    while b13_15 < 13:
        b13_15 = roll6() + 9

    # List with the three variables
    c = [b1_3, b4_6, b7_9, b10_12, b13_15]

    # Get a random number from 1 to 5
    d = roll6()
    while d > 5:
        d = roll6()

    # Pick one element from the list and print it based on variable d
    if d == 1:
        e = c[0]
    elif d == 2:
        e = c[1]
    elif d == 3:
        e = c[2]
    elif d == 4:
        e = c[3]
    elif d == 5:
        e = c[4]

    return e

# Check the probability of each number
test = []
for i in range(10000):
    test.append(roll15())
n = 1
for p in range(15):
    print(test.count(n))
    n += 1

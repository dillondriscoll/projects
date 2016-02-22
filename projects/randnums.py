import random
def randNums():
#pseudo random number generator that adds the randomly picked numbers to a total	
    total = 0
    for count in range(6):
        number = random.randrange(1, 10)
        print(number, end=' ')
        total = total + number
    print ("\nThe total is",total)

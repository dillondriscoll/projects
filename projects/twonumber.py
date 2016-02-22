def twonumberdivision():
#Checks if a number is divisible by 2 inputted integers

    mainnumber = int(input("Enter a number to check for division"))
    numberone = int(input("Enter the first number to check: "))
    numbertwo = int(input("Enter the second number to check: "))
    if mainnumber % numberone == 0 and mainnumber % numbertwo == 0:
        print("The number is divisible by ", numberone, ' and number ', numbertwo)
    elif mainnumber % numberone == 0:
        print ("The number is divisible by " + numberone)
    elif mainnumber % numbertwo == 0:
        print ("The number is divisible by " + numbertwo)
    else:
        print("You done goofed")
               

import random
import math

#these are various project I have worked on

def lgprimefactor(): 
#This program figures out the largest prime factor of whatever number is inputted.                     
    t = int(input("Enter an integer here!"))            
    f = 2                       
    p = 1                       
    while t > 1:                
        if t % f == 0:          
            p = f               
            t = t // f          
            while t % f == 0:   
                t = t // f      
        f += 1                  
    print (p) 

def shippingcalc():
#this program calculates shipping cost and can be customized for each scenario
    value = float(input("How much does your order cost?: "))

    if value >= 100.00:
        print ("shipping is free.")
    else:
        weight = float(input("How much does your order weigh: "))

        if weight >= 40:
            shipping = float(weight * 1.09)
            print ("Shipping costs: $",shipping)
        elif weight < 40:
            print("Shipping is less than 40")

def cuberoot():
            #find the cube root of a perfect cube or negative cube

    x = int(input("Enter an integer: "))
    if x>0:
        ans = x**(1./3.)
        if ans ** 3 != abs(x):
            print (x, 'is not a perfect cube!')
    else:
        ans = -((-x)**(1./3.))
        if ans ** 3 != -abs(x):
            print (x, 'is not a perfect cube!')

    print ('Cube root of ' + str(x) + ' is ' + str(ans))


        

def farenheitcalc():
#This program converts farenheit degrees to celsius
    fahrenheit = float(input("Please input temperature in degrees fahrenheit ==> "))

    convertcelsius = float((fahrenheit - 32) * float(5 / 9))

    print ('Temperature in degrees celcius is ==> ',format(convertcelsius,'.3f'))

def fractionconversion():
#This program converts improper fractions into mixed numbers
	numerator = int(input("Input the number of the numerator ==> "))

	denominator = int(input("Input the number of the denominator ==> "))

	first_number = int(numerator / denominator)
	second_number = numerator % denominator
	third_number = denominator

	print ("The mixed number equivalent is ==> ",first_number," and ",second_number,"/", third_number)

def hello():
#This is a simple hello world program with a twist
	hello = ["h","e","l","l","o"]

	print ("".join(hello))

def looper():
#This prints a table of multiples in the range of 1-9 and highlights 42   
    for row in range(1, 10):
        print()
        

        for column in range(1, 10):
            if column == 6 and row == 7 or row == 7 and column == 6:
                print(format(" >42"),end='')
            else:
                print(format(row * column,'4d'),end='')





def randNums():
#pseudo random number generator that adds the randomly picked numbers to a total	
    total = 0
    for count in range(6):
        number = random.randrange(1, 10)
        print(number, end=' ')
        total = total + number
    print ("\nThe total is",total)



def testcalculator():
#Simple test average calculator that you can exit by not inputting a number or by typing 0.
    total = 0
    count = 0
    average = 0
    data = 1


    while data != 0:
        try:
            data = int(input("Enter a number or press 0 to quit: "))
            if data == 0:
                break
            else:

                try:
                
                    count += 1
                    number = data
                    total += int(number)
                    average = total / count
                    data = int(input("Enter a number or press 0 to quit: "))
                
                except ValueError:
                    break
        except ValueError:
            break

    print("The sum is {0}. The average is {1}.".format(total, average))



def adder():
#This adds all the numbers starting from 1 together until it reaches the original inputted integer.
    usercurrent = int(input("Enter a number and this program will add together every number up to this ")) 
    digitone = 1  
    thetotal = 0
    while digitone <= usercurrent: #Adds each iteration together
        thetotal += digitone  #Adds the current digitone value to the total
        digitone += 1   #Ticks up until it reaches the original user inputted number
    print ("All of the numbers added are equal to ", thetotal)       #prints the final total

def fibonacci(n):
#Prints all of the fibonacci numbers in the range specified
    a,b = 1,1
    for i in range(n-1): 
        a, b = b, a+b  # Assigns a to b, and b to the sum of a and b moving both variables forward
    return a
def fibonacciprinter():    
    fibnumber = int(input("Select how many Fibonacci numbers to show"))
    for i in range(fibnumber):
    	print (fibonacci(i))

def twonumberdivision():
#Checks if a number is divisible by 2 inputted integers

	mainnumber = int(input("Enter a number to check for division"))
	numberone = int(input("Enter the first number to check: "))
	numbertwo = int(input("Enter the second number to check: "))




	if mainnumber % numberone == 0 and mainnumber % numbertwo == 0:
    		print("This number is divisible by ", numberone, " and ", numbertwo)
	elif mainnumber % numberone == 0:
    		print("This number is divisible by",numberone)
	elif mainnumber % numbertwo == 0:
    		print("This number is divisible by ", numbertwo)
	else:
    		print("This number is not divisible by the selected numbers.")
























	


                  

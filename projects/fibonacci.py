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

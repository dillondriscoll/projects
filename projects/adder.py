def adder():
#This adds all the numbers starting from 1 together until it reaches the original inputted integer.
    usercurrent = int(input("Enter a number and this program will add together every number up to this ")) 
    digitone = 1  
    thetotal = 0
    while digitone <= usercurrent: #Adds each iteration together
        thetotal += digitone  #Adds the current digitone value to the total
        digitone += 1   #Ticks up until it reaches the original user inputted number
    print ("All of the numbers added are equal to ", thetotal)       #prints the final total

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

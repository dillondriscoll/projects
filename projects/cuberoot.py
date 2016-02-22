import math
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


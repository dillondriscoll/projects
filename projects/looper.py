def looper():
#This prints a table of multiples in the range of 1-9 and highlights 42   
    for row in range(1, 10):
        print()
        

        for column in range(1, 10):
            if column == 6 and row == 7 or row == 7 and column == 6:
                print(format(" >42"),end='')
            else:
                print(format(row * column,'4d'),end='')

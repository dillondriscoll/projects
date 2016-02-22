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

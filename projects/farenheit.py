def farenheitcalc():
#This program converts farenheit degrees to celsius
    fahrenheit = float(input("Please input temperature in degrees fahrenheit ==> "))

    convertcelsius = float((fahrenheit - 32) * float(5 / 9))

    print ('Temperature in degrees celcius is ==> ',format(convertcelsius,'.3f'))



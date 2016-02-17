#This will link to all of my other projects with a nice menu.
import projects

def main():
    print("Welcome to my code portfolio.\n")
    menu = "1.Largest Prime Factor Calculator\n" +"2.Shipping Calculator\n"+ \
          "3.Cube Root Checker\n" + "4.Farenheit to Celsius Converter.\n" + \
          "5.Improper Fraction Converter\n" + "6.Hello World\n" + \
          "7.Multiple table with 42 highlighted \n" + \
          "8.Random number Generator\n" + "9.Test Score Average Calculator \n" + \
          "10.Program that adds all integers leading up to input \n" + \
          "11.Fibonacci List \n" + "12.Two Number Division Checker\n"
    print (menu)
    selector = ""
    while selector != "q":
        selector = (input("\n Enter the number of the program to run or" + \
                          " q to quit"))
        if selector == "1":
            projects.lgprimefactor()
        elif selector == "2":
            projects.shippingcalc()
        elif selector == "3":
            projects.cuberoot()
        elif selector == "4":
            projects.farenheitcalc()
        elif selector == "5":
            projects.fractionconversion()
        elif selector == "6":
            projects.hello()
        elif selector == "7":
            projects.looper()
        elif selector == "8":
            projects.randNums()
        elif selector == "9":
            projects.testcalculator()
        elif selector == "10":
            projects.adder()
        elif selector == "11":
            projects.fibonacciprinter()
        elif selector == "12":
            projects.twonumberdivision()
        elif selector =="m":
            print (menu)
            
        elif selector != "q":
            print("Oops, that is not a valid entry." + \
                  "Type m to bring up the menu again, " + \
                  "Type a program number or q to quit.")
    print("\nGoodbye and thanks for checking out my projects!")
          

main()
    

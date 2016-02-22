
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

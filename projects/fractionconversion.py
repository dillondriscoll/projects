def fractionconversion():
#This program converts improper fractions into mixed numbers
	numerator = int(input("Input the number of the numerator ==> "))

	denominator = int(input("Input the number of the denominator ==> "))

	first_number = int(numerator / denominator)
	second_number = numerator % denominator
	third_number = denominator

	print ("The mixed number equivalent is ==> ",first_number," and ",second_number,"/", third_number)

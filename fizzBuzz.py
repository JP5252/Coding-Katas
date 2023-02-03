def fizzBuzz(num):
	#check if num is divisble by 3 and 5
	if (num%3 == 0) and (num%5 == 0):
		num = "FizzBuzz"

	#checks if num is divisible by 3
	elif (num%3 == 0):
		num = "Fizz"
	
	#check if num is divisible by 5
	elif (num%5 == 0):
		num = "Buzz"

	#convert num to type str
	num = str(num)
	return num

def main():
	#Test 1 checking we can change from type int to str
	num1 = 10
	if (type(fizzBuzz(num1)) == int):
		print("Test 1: Failed")
	elif (type(fizzBuzz(num1)) == str):
		print("Test 1: Passed")

	#Test 2 checking that multiples of 3 return as "Fizz"
	num2 = 9
	if (fizzBuzz(num2) != "Fizz"):
		print("Test 2: Failed")
	elif (fizzBuzz(num2) == "Fizz"):
		print("Test 2: Passed")
	
	#Test 3 checking that multiples of 5 return as "Buzz"
	num3 = 10
	if (fizzBuzz(num3) != "Buzz"):
		print("Test 3: Failed")
	elif (fizzBuzz(num3) == "Buzz"):
		print("Test 3: Passed")
	
	#Test 4 checking that multiples of 3 and 5 return as "FizzBuzz"
	num4 = 15
	if (fizzBuzz(num4) != "FizzBuzz"):
		print("Test 4: Failed")
	elif (fizzBuzz(num4) == "FizzBuzz"):
		print("Test 4: Passed")

if __name__ == '__main__':
     main()
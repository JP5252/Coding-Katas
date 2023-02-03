def fizzBuzz(num):
	#checks if num is divisible by 3
	if (num%3 == 0):
		num = "Fizz"	#change name to Fizz

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
if __name__ == '__main__':
     main()
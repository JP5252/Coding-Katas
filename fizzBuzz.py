def fizzBuzz(num):
	return type(num)

def main():
	num1 = 10
	if (fizzBuzz(num1) == type(int)):
		print("Test1 Failed")
	elif (fizzBuzz(num1) == type(str)):
		print("Test1 Passed")
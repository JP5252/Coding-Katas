def fizzBuzz(num):

	return num

def main():
	num1 = 10
	if (type(fizzBuzz(num1)) == int):
		print("Test1 Failed")
	elif (type(fizzBuzz(num1)) == str):
		print("Test1 Passed")

if __name__ == '__main__':
     main()
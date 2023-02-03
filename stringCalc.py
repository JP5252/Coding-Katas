#TDD kata 2

def add(numbers):
	return -1

def main():
	#test 1 take in null/empty string input
	num1 = ""
	if (add(num1) != 0):
		print("Test 1: Failed")
	elif (add(num1) == 0):
		print("Test 1: Passed")

if __name__ == '__main__':
     main()
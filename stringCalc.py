#TDD kata 2

#takes a string input split by commas and adds then then returns as int
def add(numbers):
	if (numbers == ""):
		return 0
	else:
		return int(numbers)

def main():
	#test 1 take in null/empty string input
	num1 = ""
	if (add(num1) != 0):
		print("Test 1: Failed")
	elif (add(num1) == 0):
		print("Test 1: Passed")
	#test 1 take in null/empty string input
	num2 = "1"
	if (add(num2) != 1):
		print("Test 1: Failed")
	elif (add(num2) == 1):
		print("Test 1: Passed")

if __name__ == '__main__':
     main()
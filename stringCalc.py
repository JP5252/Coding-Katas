#TDD kata 2

#takes a string input split by commas and adds then then returns as int
def add(numbers):
	#if string is empty return 0
	if (numbers == ""):
		return 0

	#if string has multiple numbers add them
	elif ("," in numbers):
		#split numbers into list deliminated by newline
		lineList = numbers.split("\n")
		#put lines together deliminated by commas
		numbers = ",".join(lineList)
		#split numbers into list deliminated by commas
		numList = numbers.split(",")
		sum = 0
		#add and return
		for num in numList:
			sum += int(num)
		return sum
	
	#if string has just one number return as int
	else:
		return int(numbers)

def main():
	#test 1 take in null/empty string input
	num1 = ""
	if (add(num1) != 0):
		print("Test 1: Failed")
	elif (add(num1) == 0):
		print("Test 1: Passed")

	#test 2 take in string return int
	num2 = "1"
	if (add(num2) != 1):
		print("Test 1: Failed")
	elif (add(num2) == 1):
		print("Test 1: Passed")
	
	#test 3 take in string with multiple numbers split by commas return added
	num3 = "1,2"
	if (add(num3) != 3):
		print("Test 1: Failed")
	elif (add(num3) == 3):
		print("Test 1: Passed")

	#test 4 take in string with multiple numbers split by newline return added
	num4 = "1,2\n3"
	if (add(num4) != 6):
		print("Test 1: Failed")
	elif (add(num4) == 6):
		print("Test 1: Passed")

if __name__ == '__main__':
     main()
#TDD kata 2

#takes a string input split by commas and adds then then returns as int
def add(numbers):
	#initiate delim var as comma
	delim = ","

	#change delim if input starts as "//"
	if (numbers[0:1] == "/"):
		#change delim to given delim
		delim = numbers[2]
		#changes string numbers to only start after newline
		numbers = numbers[numbers.index("\n")+1:]
	
	#checking for illegal characters that are not delim or num
	for ch in numbers:
		if not (ch.isnumeric()):
			if (ch != delim and ch != "\n"):
				return ("ERROR: '" + delim + "' expected but '" + ch + \
					   "' found at position " + str(numbers.index(ch)) + ".")

	#if string is empty return 0
	if (numbers == ""):
		return 0

	#if string ends in seperator return error
	elif not (numbers[-1].isnumeric()):
		return "ERROR: Input cannot end in seperator"

	#if string has multiple numbers add them
	elif (delim in numbers):
		#split numbers into list deliminated by newline
		lineList = numbers.split("\n")
		#put lines together deliminated by commas
		numbers = delim.join(lineList)
		#split numbers into list deliminated by commas
		numList = numbers.split(delim)
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
		print("Test 2: Failed")
	elif (add(num2) == 1):
		print("Test 2: Passed")
	
	#test 3 take in string with multiple numbers split by commas return added
	num3 = "1,2"
	if (add(num3) != 3):
		print("Test 3: Failed")
	elif (add(num3) == 3):
		print("Test 3: Passed")

	#test 4 take in string with multiple numbers split by newline return added
	num4 = "1,2\n3"
	if (add(num4) != 6):
		print("Test 4: Failed")
	elif (add(num4) == 6):
		print("Test 4: Passed")

	#test 5 take in string with multiple numbers split by newline return added
	num5 = "1,2,"
	if (add(num5) != "ERROR: Input cannot end in seperator"):
		print("Test 5: Failed")
	elif (add(num5) == "ERROR: Input cannot end in seperator"):
		print("Test 5: Passed")
	
	#test 6 ability to change delimiter
	num6 = "//;\n1;3"
	if (add(num6) != 4):
		print("Test 6: Failed")
	elif (add(num6) == 4):
		print("Test 6: Passed")
	
	#test 7 checiking for invalid characters/deliminators
	num7 = "//|\n1|2,3"
	if (add(num7) != "ERROR: '|' expected but ',' found at position 3."):
		print("Test 7: Failed")
	elif (add(num7) == "ERROR: '|' expected but ',' found at position 3."):
		print("Test 7: Passed")
	
	#test 8 checiking for invalid characters/deliminators
	num8 = "-2, -9"
	if (add(num8) != "ERROR: Negative number(s) not allowed. -2, -9"):
		print("Test 8: Failed")
	elif (add(num8) == "ERROR: Negative number(s) not allowed. -2, -9"):
		print("Test 8: Passed")
	

if __name__ == '__main__':
     main()

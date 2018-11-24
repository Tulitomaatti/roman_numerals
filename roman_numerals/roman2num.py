roman_nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, "": 0}
roman_exps = {'I': 0, 'V': 0, 'X': 1, 'L': 1, 'C': 2, 'D': 2, 'M': 3, "": float('inf')}

def smallr2n(roman_str):
	# Parse roman numerals to 1-4999 
	# Assume valid input 
	num = 0
	aux = 0
	prev_c = ""

	for c in roman_str:
		# Check changes in exponent to detect decimal placement vs. subtractive notation. 
		if roman_exps[c] < roman_exps[prev_c]:
			# Previous block should be handled now 
			num += aux
			aux = roman_nums[c]

		elif roman_exps[c] > roman_exps[prev_c]: 
			# Encountered subtractive notation. 
			aux = roman_nums[c] - aux
			
		else: # Same exponent 
			if roman_nums[c] <= roman_nums[prev_c]:
				aux += roman_nums[c] # Add up repeating chars
			else: # Encountered Subtractive notation
				aux = roman_nums[c] - aux; 

		prev_c = c

	return num + aux

	# Maybe a state machine? 

	pass

def r2n(roman_str):
	return smallr2n(roman_str)


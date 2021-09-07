def is_valid_number(value):
	try:
		value = float(value)
	except:
		return False
	return True
	
print(is_valid_number("234"))
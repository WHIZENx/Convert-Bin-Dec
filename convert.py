def convert_to_dec(n):
	result = 0
	i = 0
	for count in n:
		if i == 0:
			result = -(result*2 + int(count))
		else:
			result = result*2 + int(count)
		i += 1

	return result

def convert_to_bin(n, digit):
	if n < 0:
		abs_n = abs(n)-1
	else:
		abs_n = abs(n)
	result_bin = 0
	i = 0
	while abs_n > 0:
		bin_number = abs_n % 2
		abs_n //= 2
		result_bin += bin_number*(10**i)
		i += 1

	result_bin = "".join(["0" for i in range(digit-len(str(result_bin)))] + [str(result_bin)])

	if n < 0:
		result_bin = "".join(["0" if item == "1" else "1" for item in result_bin])

	return result_bin

def convert_to_bin_signded(n, digit):
	if n < 0:
		abs_n = abs(n)-1
	else:
		abs_n = abs(n)
	result_bin = 0
	i = 0
	while abs_n > 0:
		bin_number = abs_n % 2
		abs_n //= 2
		result_bin += bin_number*(10**i)
		i += 1

	result_bin = "".join(["0" for i in range(digit-len(str(result_bin)))] + [str(result_bin)])

	if n < 0:
		result_bin = "".join(["1"] + ["0" if item == "1" else "1" for item in result_bin])
	else:
		result_bin = "".join(["0"] + [result_bin])

	return result_bin 

def two_complement(x):
	list_rev = "".join(["0" if i == "1" else "1" for i in x])
	con_to_dec = convert_to_dec(list_rev)+1
	con_to_bin = convert_to_bin(con_to_dec, len(list_rev))

	return con_to_bin

def convert_bin(n, digit):
	if len(n) < digit: n = "".join(["0" for i in range(digit-len(n))] + [n])
	else: n = n[len(n)-digit:]

	return n
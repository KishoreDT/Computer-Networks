nibble_to_bits = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]

def countSetBits(num):
	nibble = 0
	if (0 == num):
		return nibble_to_bits[0]
	nibble = num & 0xf
	return nibble_to_bits[nibble] + countSetBits(num >> 4)

def getParity(num):
	return countSetBits(num) % 2

n = 7
print("Parity of no", n, " = ", ["even", "odd"][getParity(n)])

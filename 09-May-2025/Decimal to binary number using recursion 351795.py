# Problem: Decimal to binary number using recursion - https://www.geeksforgeeks.org/decimal-binary-number-using-recursion/

def dec_to_bin_rec(d):
	if d == 0:
		return ""
	return dec_to_bin_rec(d//2) + ("0" if d%2 == 0 else "1")

def dec_to_bin(d):
	if d == 0:
		return "0"
	return dec_to_bin_rec(d)

if __name__ == '__main__':
	d = int(input())
	print(dec_to_bin_rec(d))
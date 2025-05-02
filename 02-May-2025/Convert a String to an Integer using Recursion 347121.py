# Problem: Convert a String to an Integer using Recursion - https://www.geeksforgeeks.org/convert-a-string-to-an-integer-using-recursion/

def stoi(s : str):
    if len(s) == 1:
        return ord(s) - ord("0")
    return ord(s[-1]) - ord("0") + 10*stoi(s[:-1])

a = input()
print(stoi(a))
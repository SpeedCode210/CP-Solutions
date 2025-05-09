# Problem: Recursively remove all adjacent duplicates - https://www.geeksforgeeks.org/recursively-remove-adjacent-duplicates-given-string/

#User function Template for python3

class Solution:
    def removeUtil (self, S):
		s = "$" + S + "$"
		res = "".join(s[i] for i in range(1, len(S)+1) if s[i] != s[i-1] and s[i] != s[i+1])
		if len(S) == len(res):
		    return S
		else:
		    return self.removeUtil(res)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        s = ob.removeUtil(S)
        if len(s) == 0:
            print("\"\"")
        else:
            print(s)

        print("~")

# } Driver Code Ends
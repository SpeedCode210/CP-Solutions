# Problem: Array Subset - https://practice.geeksforgeeks.org/problems/array-subset-of-another-array2317/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab

#User function Template for python3

class Solution:
    def isSubset(self, a, b):
        A = dict([(-1,0)])
        B = dict([(-1,0)])
        for x in a:
            if x in A:
                A[x] += 1
            else:
                A[x] = 1
        for x in b:
            if x in B:
                B[x] += 1
            else:
                B[x] = 1
                
        for key in B:
            if not(key in A):
                return False
            if A[key] < B[key]:
                return False
        return True
    
    
    
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        ob = Solution()
        if ob.isSubset(a1, a2):
            print("true")
        else:
            print("false")

        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
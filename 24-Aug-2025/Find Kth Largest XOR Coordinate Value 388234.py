# Problem: Find Kth Largest XOR Coordinate Value - https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/description/?envType=problem-list-v2&envId=bit-manipulation

from heapq import heappush, heappop
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        S = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == j == 0:
                    pass
                elif i == 0:
                    matrix[i][j] ^= matrix[i][j-1]
                elif j == 0:
                    matrix[i][j] ^= matrix[i-1][j]
                else:
                    matrix[i][j] ^= matrix[i-1][j]^matrix[i][j-1]^matrix[i-1][j-1]
                
                S.append(matrix[i][j])

        return sorted(S)[max(-k, -len(S))]

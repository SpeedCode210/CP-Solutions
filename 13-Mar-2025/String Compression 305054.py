# Problem: String Compression - https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        counter = 0
        char = ""
        res = ""
        index = 0
        l = 0
        for c in chars:
            if c == char:
                counter+=1
            else:
                res = char + ("" if counter <= 1 else str(counter))
                counter = 1
                char = c
                l += len(res)
                for i in range(index, index+len(res)):
                    chars[i] = res[i-index]
                index += len(res)
        
        res = char + ("" if counter <= 1 else str(counter))
        l += len(res)
        for i in range(index, index+len(res)):
            chars[i] = res[i-index]
            
        index += len(res)
        
        return l
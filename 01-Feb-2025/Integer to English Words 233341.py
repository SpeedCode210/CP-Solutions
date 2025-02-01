# Problem: Integer to English Words - https://leetcode.com/problems/integer-to-english-words/

names = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine",
        "Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen", "Sixteen","Seventeen","Eighteen","Nineteen"]
nbs = ["Zero","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]

class Solution:
    
    def chunk(self, num: int) -> str:
        res = ""
        if (num // 100)%10 > 0 :
            res += names[(num//100)%10] + " Hundred "
        if (num // 10)%10 > 1:
            res += nbs[(num // 10)%10] + " "
            if num%10 > 0:
                res += names[num%10] + " "
        elif num % 100 > 0:
            res += names[num%100] + " "
        return res

    def numberToWords(self, num: int) -> str:
        if num==0:
            return "Zero"
        result = ""
        if num >= 1000000000:
            result = names[num//1000000000] + " Billion "
        if (num // 1000000)%1000 > 0 :
            result += self.chunk(num // 1000000) + "Million "
        if (num // 1000) % 1000 > 0 :
            result += self.chunk((num // 1000) % 1000) + "Thousand "
        if num % 1000 > 0 :
            result += self.chunk(num % 1000)
        return result[:-1]
        
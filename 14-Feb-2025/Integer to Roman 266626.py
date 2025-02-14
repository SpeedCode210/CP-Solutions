# Problem: Integer to Roman - https://leetcode.com/problems/integer-to-roman/description/

class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        if num >= 1000:
            res += "M"*(num // 1000)
            num -= (num // 1000)*1000

        if num >= 900:
            res += "CM"
            num -= 900

        if num >= 500:
            res += "D"
            num -= 500

        if num >= 400:
            res += "CD"
            num -= 400

        if num >= 100:
            res += "C"*(num//100)
            num -= 100*(num//100)

        if num >= 90:
            res += "XC"
            num -= 90

        if num >= 50:
            res += "L"
            num -= 50

        if num >= 40:
            res += "XL"
            num -= 40

        if num >= 10:
            res += "X"*(num//10)
            num -= 10*(num//10)

        if num >= 9:
            res += "IX"
            num -= 9

        if num >= 5:
            res += "V"
            num -= 5

        if num >= 4:
            res += "IV"
            num -= 4

        if num >= 1:
            res += "I"*num


        return res
# Problem: Decode XORed Permutation - https://leetcode.com/problems/decode-xored-permutation/description/?envType=problem-list-v2&envId=bit-manipulation

class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        encoded = [0] + encoded
        mask = 1
        for i in range(1, len(encoded)):
            encoded[i] ^= encoded[i-1]
            mask ^= encoded[i]
            mask ^= i+1

        for i in range(0, len(encoded)):
            encoded[i] ^= mask

        return encoded

class Solution:
    def hammingWeight(self, n: int) -> int:
        x = bin(n)[2:]
        n = 0
        for i in x:
            if i == '1':
                n += 1
            else:
                continue
        return n

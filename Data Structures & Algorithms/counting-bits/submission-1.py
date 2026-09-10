class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n+1):
            # x = bin(i)[2:]
            # output.append(x.count('1'))
            output.append(i.bit_count())
        return output 

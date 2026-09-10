class Solution:
    def reverseBits(self, n: int) -> int:
        if n > 0:
            n = n & 0xFFFFFFFF
        
        n = str(f'{n:032b}')
        return int(n[::-1],2)

  

        
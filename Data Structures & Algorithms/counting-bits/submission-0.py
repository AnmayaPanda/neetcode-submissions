class Solution:
    def countBits(self, n: int) -> List[int]:
        def hammingWeight(n):
            count = 0
            while n:
                if n&1:
                    count += 1
                n >>= 1
            return count
        
        result = [hammingWeight(num) for num in range(0,n+1)]
        return result
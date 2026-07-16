class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        if n == 0:
            return float(1)
        while n != 0: 
            if n > 0:
                result *= x
                print(n, result)
                n -= 1
                
            else:
                result /= x
                print(n, result)
                n += 1
               
        return result
            

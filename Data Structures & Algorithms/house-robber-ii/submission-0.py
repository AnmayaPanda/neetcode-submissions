class Solution:
    def rob(self, nums: List[int]) -> int:
        def robLinear(numbers):
            num_len = len(numbers)
            if num_len == 1:
                return numbers[0]
            if num_len == 2:
                return max(numbers[0], numbers[1])
            
            dp = [0]*num_len
            dp[0] = numbers[0]
            dp[1] = max(numbers[0], numbers[1])

            for i in range(2, num_len):
                dp[i] = max(dp[i-1], dp[i-2] + numbers[i])
            
            return dp[-1]
        if len(nums) == 1:
            return nums[0]
        return max(robLinear(nums[:-1]), robLinear(nums[1:]))
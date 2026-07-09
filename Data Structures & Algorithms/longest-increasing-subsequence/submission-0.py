class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n
        for i in range(n):
            dp[i] = 1
            for j in range(i):
                if nums[j] < nums[i] and dp[i] < 1 + dp[j]:
                    dp[i] = 1 + dp[j]
            
        return max(dp)
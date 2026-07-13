class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        freq = Counter(nums)

        for key in freq:
            if freq[key] > len(nums)//2:
                return key
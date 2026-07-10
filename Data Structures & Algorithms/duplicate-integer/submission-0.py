class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        freq = Counter(nums)

        return any(v>1 for v in freq.values())
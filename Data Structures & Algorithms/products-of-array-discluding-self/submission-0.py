class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProd = [0]*len(nums)
        prefixProd[0] = 1
        postProd = [0]*len(nums)
        postProd[len(nums)-1] = 1
        for i in range(1,len(nums)):
            prefixProd[i] = prefixProd[i-1]*nums[i-1]
            postProd[-i-1] = postProd[-i]*nums[-i]

        for i in range(len(nums)):
            nums[i] = prefixProd[i]*postProd[i]
        return nums
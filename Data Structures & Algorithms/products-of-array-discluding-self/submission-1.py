class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)
        
        running_product = 1
        for i in range(1, len(nums)):
            res[i] = running_product * nums[i - 1]
            running_product = res[i]

        running_product = 1
        for i in reversed(range(len(nums))):
            res[i] = res[i] *  running_product
            running_product = running_product * nums[i]

        return res



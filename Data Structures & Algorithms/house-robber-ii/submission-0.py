class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) <= 2:
            return max(nums)
        maxAmountIncludeOne = [0] * (n - 1)
        maxAmountExcludeOne = [0] * (n - 1)
        
        maxAmountIncludeOne[0], maxAmountIncludeOne[1] = nums[0], max(nums[0], nums[1])

        maxAmountExcludeOne[0], maxAmountExcludeOne[1] = nums[1], max(nums[1], nums[2])

        for i in range(2, n - 1):
            maxAmountIncludeOne[i] = max(maxAmountIncludeOne[i - 1], maxAmountIncludeOne[i - 2] + nums[i])
        
        for i in range(2, n - 1):
            maxAmountExcludeOne[i] = max(maxAmountExcludeOne[i - 1], maxAmountExcludeOne[i - 2] + nums[i + 1])
        
        
        return max(maxAmountExcludeOne[n - 2], maxAmountIncludeOne[n - 2])


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
            
        n = len(nums)
        maxAmount = [0] * n
        maxAmount[0] = nums[0]
        maxAmount[1] = max(nums[0], nums[1])

        for i in range(2, n):
            maxAmount[i] = max(maxAmount[i - 1], maxAmount[i - 2] + nums[i])
        
        return maxAmount[n - 1]

        
        # maxAmount[n - 1] = nums[n - 1]
        # maxAmount[n - 2] = nums[n - 2]

        # for i in reversed(range(0, n - 2)):
        #     maxAmount[i] = max(maxAmount[i + 1], nums[i] + maxAmount[i + 2])

        # return maxAmount[0]
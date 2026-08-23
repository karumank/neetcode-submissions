class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
            
        n = len(nums)
        maxAmount = [0] * n
        prev = nums[0]
        curr = max(nums[0], nums[1])

        for i in range(2, n):
            prev, curr = curr, max(curr, prev + nums[i])
        
        return curr
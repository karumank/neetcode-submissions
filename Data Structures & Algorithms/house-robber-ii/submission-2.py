class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        
        prevIncludeOne, currIncludeOne = nums[0], max(nums[0], nums[1])

        prevExcludeOne, currExcludeOne = nums[1], max(nums[1], nums[2])

        for i in range(2, n - 1):
            prevIncludeOne,  currIncludeOne = currIncludeOne, max(currIncludeOne, prevIncludeOne + nums[i])
        
        for i in range(2, n - 1):
            prevExcludeOne, currExcludeOne = currExcludeOne, max(currExcludeOne, prevExcludeOne + nums[i + 1])
        
        
        return max(currIncludeOne, currExcludeOne)


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        min_result = float("inf")
        while left <= right:

            if nums[left] < nums[right]:
                return min(min_result, nums[left])

            mid = (left + right) // 2
            min_result = min(min_result, nums[mid])

            if nums[mid] < nums[right]:
                right = mid - 1
            elif nums[mid] >= nums[right]:
                left = mid + 1

        return min_result
            

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result_set = set()
        for i in range(len(nums)):
            target = -nums[i] 
            left = i + 1
            right = len(nums) - 1

            while left < right: 
                curr_sum = nums[left] + nums[right]
                if curr_sum > target:
                    right -= 1
                elif curr_sum < target:
                    left += 1
                else:
                    result_set.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
        return list(result_set)

                



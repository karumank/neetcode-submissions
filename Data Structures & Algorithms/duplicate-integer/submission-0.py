class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_count = {}
        for n in nums:
            if n in num_count:
                return True
            else:
                num_count[n] = n
        return False
        
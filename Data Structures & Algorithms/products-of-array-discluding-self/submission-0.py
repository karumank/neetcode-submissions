class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_prefix = [1]
        product_suffix = [1]
        curr_product = 1
        for num in nums:
            curr_product *= num
            product_prefix.append(curr_product)
        # [1, 1, 2, 8, 48]
        curr_product = 1
        for i in reversed(range(len(nums))):
            curr_num = nums[i]
            curr_product *= curr_num
            product_suffix.insert(0, curr_product)
        # [48, 48, 24, 6, 1]
        result = []

        for i in range(len(nums)):
            prefix_val = product_prefix[i] 
            suffix_val = product_suffix[i + 1]
            result.append(prefix_val * suffix_val)
        # [48, 24, 12, 8]
        return result


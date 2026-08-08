import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles) # 4
        result = float('inf')
        while left <= right:
            mid = (left + right) // 2 # 2 Banana' s per hr
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)

            if hours <= h:
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result
            


import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)

        result = float("inf")
        while left <= right:
            mid = (left + right) // 2

            eating_time = 0
            for pile in piles:
                eating_time += math.ceil(pile / mid)
            
            if eating_time > h:
                left = mid + 1
            elif eating_time <= h:
                result = min(result, mid)
                right = mid - 1
        return result
            

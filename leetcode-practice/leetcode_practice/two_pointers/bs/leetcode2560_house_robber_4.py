from typing import List


class Solution:
    def house_robber_iv(self, nums: List[int], k: int) -> int:
        low = min(nums)
        high = max(nums)

        # Find the target between [low, high] that is the max of at least k houses

        def houses_below(wealth: int) -> int:
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= wealth:
                    count += 1
                    i += 1
                i += 1
            return count
        
        while low < high:
            mid = low + (high - low) // 2
            if houses_below(mid) >= k:
                high = mid
            else:
                low = mid + 1

        return low

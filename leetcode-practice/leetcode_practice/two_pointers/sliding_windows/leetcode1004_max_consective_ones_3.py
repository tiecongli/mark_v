from typing import List

class Solution:
    def max_consective_ones_iii(self, nums: List[int], k: int) -> int:
        zero_count = 0
        longest = 0
        i = 0

        for j in range(len(nums)):
            if nums[j] == 0:
                zero_count += 1
            
            while zero_count > k:
                if nums[i] == 0:
                    zero_count -= 1
                i += 1
            
            longest = max(longest, j - i + 1)

        return longest
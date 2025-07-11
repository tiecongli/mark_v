from typing import List

class Solution:
    def max_consective_ones_ii(self, nums: List[int]) -> int:
        i = 0
        zero_count = 0
        max_len = 0

        for j in range(len(nums)):
            if nums[j] == 0:
                zero_count += 1
            while zero_count > 1:
                if nums[i] == 0:
                    zero_count -= 1
                i += 1
            
            max_len = max(max_len, j - i + 1)
        
        return max_len
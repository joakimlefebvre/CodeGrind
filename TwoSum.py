from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            additional = target - num
            if additional in nums and nums.index(additional) != i:
                return sorted([i,nums.index(additional)])

s = Solution()
print(s.twoSum([3,2,4], 6))
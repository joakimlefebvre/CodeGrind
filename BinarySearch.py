from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            if target < nums[m]:
                r = m - 1
            if target == nums[m]:
                return m
        return -1


if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    solution = Solution()
    print(solution.search(nums, target))

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r =0,len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m]==target:
                return m
            elif nums[m]>target:
                r = m - 1
            elif nums[m]<target:
                l = m + 1
        return l


if __name__ == '__main__':
    s = Solution()
    nums = [1, 3, 5, 6]
    target = 5
    result = s.searchInsert(nums, target)
    print(result)
from typing import List

class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        max_length = 0
        length = 0
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1 and length % 2 == 0:
                length += 1
            elif nums[i+1] - nums[i] == -1 and length % 2 == 1:
                length += 1
            elif nums[i+1] - nums[i] == 1 and length % 2 != 0:
                length = 1
            else:
                length = 0
            if max_length < length:
                max_length = length
        if max_length == 0:
            return -1
        return max_length + 1

if __name__ == '__main__':
    s = Solution()
    nums = [4,5,6]
    sol = s.alternatingSubarray(nums)
    print(sol)
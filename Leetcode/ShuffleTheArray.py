from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        new_list = []
        for i in range(n):
            new_list.append(nums[i])
            new_list.append(nums[i+n])
        return new_list


if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,4,4,3,2,1]
    n = 4
    print(s.shuffle(nums, n))
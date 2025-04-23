from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums)//2
        setNum = list(set(nums))
        for num in setNum:
            if nums.count(num) > majority:
                return num


if __name__ == "__main__":
    solution = Solution()
    nums = [2,2,1,1,1,2,2]
    print(solution.majorityElement(nums))
from typing import List

class Solution1:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        quadruples = []
        nums.sort()
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j] == nums[j - 1]:
                    continue
                l, r = j + 1, len(nums) - 1
                while l < r:
                    total = num + nums[j] + nums[l] + nums[r]
                    if total > target:
                        r -= 1
                    elif total < target:
                        l += 1
                    else:
                        quadruples.append([num, nums[j], nums[l], nums[r]])
                        l += 1
                        while nums[l] == nums[l - 1] and l < r:
                            l += 1
        return quadruples

class Solution2:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, quadruples = [], []

        def kSum(k, start, target):
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    quadruples.append(nums[i])
                    kSum(k-1, i+1, target - nums[i])
                    quadruples.pop()
                return
            l, r = start, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.append(quadruples + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        kSum(4, 0, target)
        return res


if __name__ == '__main__':
    s = Solution2()
    nums = [2,2,1,2,2,1,0,0,4]
    target = 8
    res = s.fourSum(nums, target)
    print(res)
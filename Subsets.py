from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        listOfSubsets = [[]]
        for i, num in enumerate(nums):
            listOfSubsets.append([num])
            if i > 0:
                for j in range(1, len(listOfSubsets)-1):
                    combined = [num] + listOfSubsets[j]
                    combined.sort()
                    listOfSubsets.append(combined)
        return listOfSubsets


if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3]
    print(s.subsets(nums))
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n > 0:
            j = 0
            for i in range(m, m+n):
                nums1[i] = nums2[j]
                j +=1
            nums1.sort()

if __name__ == '__main__':
    solution = Solution()
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    solution.merge(nums1, m, nums2, n)
    print(nums1)
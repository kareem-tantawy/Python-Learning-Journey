# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        k = 1
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                del nums[i]
            else:
                k += 1
                i += 1
        return k

# Given an integer array nums sorted in non-decreasing order,
# remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same.
# Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted,
# you need to do the following things:

# Change the array nums such that the first k elements of nums contain the
# unique elements in the order they were present in nums initially.
# The remaining elements of nums are not important as well as the size of nums.
# Return k.
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp_nums = sorted(list(set(nums.copy())))

        nums.clear()
        nums.extend(temp_nums)

        return len(nums)


nums_1 = [-1, 0, 0, 0, 3, 3]
nums_2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
test = Solution()
# print()
print(test.removeDuplicates(nums_1))
print(nums_1)
print(test.removeDuplicates(nums_2))
print(nums_2)

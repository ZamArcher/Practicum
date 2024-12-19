# Given an integer array nums and an integer val, remove all occurrences of val
# in nums in-place. The order of the elements may be changed. Then return the
# number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k,
# to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the
# elements which are not equal to val. The remaining elements of nums are not
# important as well as the size of nums.

# Return k.
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp_nums = [i for i in nums if i != val]
        nums.clear()
        nums.extend(temp_nums)
        return len(temp_nums)


nums_1 = []
val_1 = 3
nums_2 = [0, 1, 2, 2, 3, 0, 4, 2]
val_2 = 2
test = Solution()
print(test.removeElement(nums_1, val_1))
print(nums_1)
print(test.removeElement(nums_2, val_2))
print(nums_2)
# ---------------- alter
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         index = 0
#         for i in range(len(nums)):
#             if nums[i] != val:
#                 nums[index] = nums[i]
#                 index += 1
#         return index
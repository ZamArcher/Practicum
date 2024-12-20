# Given a sorted array of distinct integers and a target value,
# return the index if the target is found. If not, return the index where
# it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.
from typing import List


# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         left_idx = 0
#         right_idx = len(nums) - 1
#         while left_idx <= right_idx:
#             mid = (right_idx + left_idx) // 2
#             if target < nums[mid]:
#                 right_idx = mid - 1
#             elif target > nums[mid]:
#                 left_idx = mid + 1
#             else:
#                 return mid

#         return left_idx


# ------------ alter
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left_idx = 0
        right_idx = len(nums) - 1
        while left_idx <= right_idx:
            mid = (right_idx + left_idx) // 2
            diff = target - nums[mid]
            if diff < 0:
                right_idx = mid - 1
            elif diff > 0:
                left_idx = mid + 1
            else:
                return mid

        return left_idx


test = Solution()
nums_1 = [1, 3, 5, 6]
target_1 = 5
nums_2 = [1, 3, 5, 6]
target_2 = 2
nums_3 = [1, 3, 5, 6]
target_3 = 7
nums_4 = [1, 3, 5, 6]
target_4 = 0


assert test.searchInsert(nums_1, target_1) == 2
assert test.searchInsert(nums_2, target_2) == 1
assert test.searchInsert(nums_3, target_3) == 4
assert test.searchInsert(nums_4, target_4) == 0

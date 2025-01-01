"""66. Plus One.

You are given a large integer represented as an integer array digits,
where each digits[i] is the ith digit of the integer. The digits are ordered
from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        addition = 1
        for i in range(len(digits) - 1, -1, -1):
            # print(digits[i])
            digits[i] = digits[i] + addition
            addition = digits[i] // 10
            digits[i] %= 10

        if addition:
            digits.insert(0, addition)

        return digits


if __name__ == '__main__':
    test_1 = [1, 2, 3]
    test_2 = [4, 3, 2, 1]
    test_3 = [9]

    large_int = Solution()

    # print(large_int.plusOne(test_1))

    assert large_int.plusOne(test_1) == [1, 2, 4]
    assert large_int.plusOne(test_2) == [4, 3, 2, 2]
    assert large_int.plusOne(test_3) == [1, 0]

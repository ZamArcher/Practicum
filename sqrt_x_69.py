"""69.Sqrt(x).

Given a non-negative integer x, return the square root of x rounded down to
the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        return right


test = Solution()
assert test.mySqrt(0) == 0
assert test.mySqrt(4) == 2
assert test.mySqrt(8) == 2
assert test.mySqrt(10) == 3
assert test.mySqrt(3364) == 58
# print(test.mySqrt(10))

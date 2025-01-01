"""67. Add Binary.

Given two binary strings a and b, return their sum as a binary string.
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num_a = int(a, 2)
        num_b = int(b, 2)
        binary_sum = bin(num_a + num_b)
        return str(binary_sum)[2:]


if __name__ == '__main__':
    binary_sum = Solution()

    # print(large_int.plusOne(test_1))

    assert binary_sum.addBinary('11', '1') == '100'
    assert binary_sum.addBinary('1010', '1011') == '10101'

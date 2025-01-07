"""70. Climbing Stairs.

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you
climb to the top?
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        temp, possible_ways = 0, 1
        for _ in range(n):
            temp, possible_ways = possible_ways, temp + possible_ways
        return possible_ways


if __name__ == '__main__':
    possible_ways = Solution()

    # print(possible_ways.climbStairs(4))
    assert possible_ways.climbStairs(1) == 1
    assert possible_ways.climbStairs(2) == 2
    assert possible_ways.climbStairs(3) == 3
    assert possible_ways.climbStairs(4) == 5
    assert possible_ways.climbStairs(5) == 8

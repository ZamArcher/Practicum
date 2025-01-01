"""58. Lenght of last word.

Given a string s consisting of words and spaces, return the length of the last
word in the string.

A word is a maximal substring consisting of non-space characters only.
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        clean_str = s.strip().split()
        return len(clean_str[-1])


if __name__ == '__main__':
    # ordered = int(input())
    # ordered_stones = [int(i) for i in input().split()]
    # devivered = int(input())
    # delivered_stones = [int(i) for i in input().split()]

    # print(count_matching_stones(ordered_stones, delivered_stones))

    test_1 = 'Hello World'
    test_2 = '   fly me   to   the moon  '
    test_3 = 'luffy is still joyboy'

    s = Solution()

    assert s.lengthOfLastWord(test_1) == 5
    assert s.lengthOfLastWord(test_2) == 4
    assert s.lengthOfLastWord(test_3) == 6

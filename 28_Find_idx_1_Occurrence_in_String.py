# Given two strings needle and haystack, return the index of the first
# occurrence of needle in haystack, or -1 if needle is not part of haystack.


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle) if needle in haystack else -1


haystack_1 = 'sadbutsad'
needle_1 = 'sad'
haystack_2 = 'leetcode'
needle_2 = 'leeto'

test = Solution()
print(test.strStr(haystack_1, needle_1))
print(test.strStr(haystack_2, needle_2))


# ------------- alter

# class Solution:
#     def strStr(self, haystack, needle):
#         for i in range(len(haystack) - len(needle) + 1):
#             if haystack[i:i+len(needle)] == needle:
#                 return i
#         return -1
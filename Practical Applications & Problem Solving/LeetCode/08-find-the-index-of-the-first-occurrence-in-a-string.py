# Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Early return if needle is longer than haystack
        if len(needle) > len(haystack):
            return -1

        # Iterate through haystack, checking for needle matches
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                return i

        # Needle not found
        return -1

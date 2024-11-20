# Link: https://leetcode.com/problems/longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]
        final = ""
        i = 1
        while i < len(strs):
            j = 0
            while j < len(strs[i]) and j < len(first):
                if first[j] == strs[i][j]:
                    final += first[j]
                else: break
                j += 1
            first = final
            final = ""
            i += 1
        return first
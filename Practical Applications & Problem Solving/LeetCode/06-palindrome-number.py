# Link: https://leetcode.com/problems/palindrome-number/


class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)  # convert int to string
        i = 0
        j = len(s) - 1
        while i < len(s):
            if s[i] != s[j]:  # at this point the number isn't palindrome!
                return False
            i += 1
            j -= 1
        return True  # If the condition doesn't happen in any iteration
                     # then the number is a palindrome number

# Note that we could also solve it using this line of code 
"""
    s = int(X)
    return s == s[::-1]     # This [::-1] reverse the string
                            # if it's palindrome then the reversed string
                            # will be the same as the original one
"""
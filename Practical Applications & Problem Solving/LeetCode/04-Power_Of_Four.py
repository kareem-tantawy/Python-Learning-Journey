# Link: https://leetcode.com/problems/power-of-four/


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        """
        Determines if the given integer `n` is a power of four.

        Args:
            n: The integer to check.

        Returns:
            True if `n` is a power of four, False otherwise.
        """

        # Base cases:
        if n < 4:
            # If n is 1, it's a power of four (4^0).
            if n == 1:
                return True
            # Otherwise, it's not a power of four.
            else:
                return False

        # Recursive case:
        # If n is greater than or equal to 4, check if n/4 is a power of four.
        # This is because a power of four divided by 4 is still a power of four.
        else:
            return self.isPowerOfFour(n / 4)

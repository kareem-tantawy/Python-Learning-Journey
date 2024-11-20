# Link : https://leetcode.com/problems/power-of-three/


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        """
        Determines if the given integer `n` is a power of three.

        Args:
            n: The integer to check.

        Returns:
            True if `n` is a power of three, False otherwise.
        """

        # Base cases:
        if n < 3:
            # If n is 1, it's a power of three (3^0).
            if n == 1:
                return True
            # Otherwise, it's not a power of three.
            else:
                return False

        # Recursive case:
        # If n is greater than or equal to 3, check if n/3 is a power of three.
        # This is because a power of three divided by 3 is still a power of three.
        else:
            return self.isPowerOfThree(n / 3)

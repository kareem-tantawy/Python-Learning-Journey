# Link: https://leetcode.com/problems/power-of-two/


def isPowerOfTwo(self, n: int) -> bool:
    """
    Determines if the given integer `n` is a power of two.

    Args:
        n: The integer to check.

    Returns:
        True if `n` is a power of two, False otherwise.
    """

    # Base cases:
    if n >= 0 and n < 2:
        # If n is 1, it's a power of two (2^0).
        if n == 1:
            return True
        # Otherwise, it's not a power of two.
        else:
            return False

    # Recursive case:
    # If n is greater than 1, check if n/2 is a power of two.
    # This is because a power of two divided by 2 is still a power of two.
    else:
        return self.isPowerOfTwo(n / 2)

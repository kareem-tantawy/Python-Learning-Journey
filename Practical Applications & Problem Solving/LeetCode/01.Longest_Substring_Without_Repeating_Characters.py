# URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

def lengthOfLongestSubstring(self, s: str) -> int:
    """
    Finds the length of the longest substring without repeating characters.

    Args:
        s: The input string.

    Returns:
        The length of the longest substring.
    """

    # If the string is empty, return 0
    if not s:
        return 0

    # Initialize the maximum length and the current substring
    max_length = 1
    current_substring = s[0]

    # Iterate over the string, starting from the second character
    for i in range(1, len(s)):
        # If the current character is already in the substring
        if s[i] in current_substring:
            # Find the index of the first occurrence of the character
            index = current_substring.index(s[i])
            # Update the substring, keeping only the characters after the first occurrence
            current_substring = current_substring[index+1:] + s[i]
        else:
            # Append the current character to the substring
            current_substring += s[i]

        # Update the maximum length if the current substring is longer
        max_length = max(max_length, len(current_substring))

    return max_length
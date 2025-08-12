"""
Assignment 4 Problem 3: Fuzzy Matching
July 30, 2025
Johnpaul Nnaji
"""

def fuzzyMatching(subOne, subTwo, sub_len):
    """
    Returns a tuple of indices where subOne and subTwo match in all but one character.
    The sub_len parameter defines how many characters to compare.
    """
    indices = []
    for i in range(len(subOne) - sub_len + 1):
        # extract substring of length sub_len from subOne
        candidate = subOne[i:i+sub_len]
        # compare with subTwo (same length)
        if len(candidate) == sub_len and len(subTwo) == sub_len:
            differences = sum(1 for a, b in zip(candidate, subTwo) if a != b)
            if differences == 1:
                indices.append(i)
    return tuple(indices)


# ----------------------------
# Testing (comment out before submission)
# ----------------------------
# Example 1
# subOne = "datascience"
# subTwo = "datx"
# sub_len = 4
# print("Fuzzy match indices:", fuzzyMatching(subOne, subTwo, sub_len))  
# Expected: (0,)

# Example 2
# subOne = "banana bandana"
# subTwo = "anb"
# sub_len = 3
# print("Fuzzy match indices:", fuzzyMatching(subOne, subTwo, sub_len))  
# (1, 3, 5, 8, 11) because each of these substrings differs from 'anb' by exactly one character, including spaces when applicable.

"""
Assignment 4 Problem 4: Fuzzy Matches Only
July 30, 2025
Johnpaul Nnaji
"""

def fuzzyMatchesOnly(srch_str, sub_str):
    """
    Returns a tuple of indices where srch_str has substrings that differ from sub_str
    by exactly one character (fuzzy matches). Exact matches are excluded.
    Uses overlapping windows.
    """
    indices = []
    sub_len = len(sub_str)
    for i in range(len(srch_str) - sub_len + 1):
        candidate = srch_str[i:i+sub_len]
        if len(candidate) == sub_len:
            differences = sum(1 for a, b in zip(candidate, sub_str) if a != b)
            if differences == 1:  # fuzzy match only
                indices.append(i)
    return tuple(indices)


# ----------------------------
# Testing (comment out before submission)
# ----------------------------
# Example 1
# srch_str = "banana bandana"
# sub_str = "ana"
# print("Fuzzy matches only:", fuzzyMatchesOnly(srch_str, sub_str))
# Expected: (8,) because only 'and' differs from 'ana' by exactly one character.

# Example 2
# srch_str = "datascience datx daty"
# sub_str = "datx"
# print("Fuzzy matches only:", fuzzyMatchesOnly(srch_str, sub_str))
# Expected: (0, 17)
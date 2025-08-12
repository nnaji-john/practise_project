"""
Assignment 4 Problem 1: Counting substring matches (iterative and recursive)
July 30, 2025
Johnpaul Nnaji
"""

# Iterative approach using str.find()
def countSubstrMatches(srch_str, sub_str):
    """
    Counts the number of NON-OVERLAPPING matches of sub_str in srch_str.
    """
    count = 0
    start = 0
    while True:
        index = srch_str.find(sub_str, start)
        if index == -1:  # no more matches
            break
        count += 1
        # Non-overlapping: move past the whole substring
        start = index + len(sub_str)
    return count

# Recursive approach using str.find()
def countSubstrRecursive(srch_str, sub_str, start=0):
    """
    Recursively counts the number of NON-OVERLAPPING matches.
    """
    index = srch_str.find(sub_str, start)
    if index == -1:  # base case
        return 0
    # move past the whole substring (non-overlapping)
    return 1 + countSubstrRecursive(srch_str, sub_str, index + len(sub_str))


# ----------------------------
# Testing (comment out before submission)
# ----------------------------
# test_str = "banana bandana banana"
# sub_str = "ana"
# print("Iterative count:", countSubstrMatches(test_str, sub_str))  # Expected: 3
# print("Recursive count:", countSubstrRecursive(test_str, sub_str))  # Expected: 3

# test_str2 = "atatattta"
# sub_str2 = "ata"
# print("Iterative count:", countSubstrMatches(test_str2, sub_str2))  # Expected: 1
# print("Recursive count:", countSubstrRecursive(test_str2, sub_str2))  # Expected: 1

"""
Assignment 4 Problem 2: Returning all indices of a substring
July 30, 2025
Johnpaul Nnaji
"""

def allMatchesIndices(srch_str, sub_str):
    """
    Returns a tuple of all starting indices where sub_str occurs in srch_str.
    Matches are NON-OVERLAPPING, consistent with Problem 1.
    """
    indices = []
    start = 0
    while True:
        index = srch_str.find(sub_str, start)
        if index == -1:  # no more matches
            break
        indices.append(index)
        start = index + len(sub_str)  # move past this match
    return tuple(indices)


# ----------------------------
# Testing (comment out before submission)
# ----------------------------
# test_str = "banana bandana banana"
# sub_str = "ana"
# print("Indices:", allMatchesIndices(test_str, sub_str))  
# # Expected: (1, 11, 16)

# test_str2 = "atatattta"
# sub_str2 = "ata"
# print("Indices:", allMatchesIndices(test_str2, sub_str2))  
# # Expected: (0,)

# test_str3 = "python"
# sub_str3 = "Java"
# print("Indices:", allMatchesIndices(test_str3, sub_str3))  
# # Expected: ()

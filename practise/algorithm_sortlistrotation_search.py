"""
Johnpaul Nnaji
Date: 2023-10-30
This script contains two functions to count the number of times a sorted list has been rotated.
The first function uses a linear search approach, while the second function uses a binary search approach.
The script also includes test cases to validate the functionality of both methods.
"""

# linear search to count the number of times a sorted list has been rotated
def count_rotation(nums):
    # Create a variable positon and set it to 1
    position = 1
    # Compare the number at position with the number before it
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            # If the number at position is less than the number before it, return position
            return position
        position += 1
    return 0  # If no rotation is found, return 0


# Binary search to count the minimum number of rotations
def count_rotation_binary_search(nums):
    if not nums:
        return 0

    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return left


# rotated  3 times
test = {
    'input' : {
        'nums' : [19, 25, 29, 3, 5, 6, 7, 9, 11]
    },
    'output' : 3
}

nums0 = test['input']['nums']
output0 = test['output']

result0 = count_rotation(nums0)

if result0 == output0:
    print("Test case passed")
else:
    print("Test case failed. Expected", output0, "but got", result0)

test0 = test

# rotated 8 times
test1 = {
    'input': {
        'nums': [3, 4, 5, 7, 8, 1, 2]
    },
    'output': 5
}

# a list that is not rotated
test2 = {
    'input': {
        'nums': [1, 2, 3, 7]
    },
    'output': 0
}

# A list that is rotated 1 time
test3 = {
    'input': {
        'nums': [5, 1, 2, 3, 4]
    },
    'output': 1
}

# A list that is rotated n-1 times
test4 = {
    'input': {
        'nums': [2, 3, 4, 5, 6, 7, 8, 1]
    },
    'output': 7
}

# A list that is rotated n times where n is the length of the list 
test5 = {
    'input': {
        'nums': [1, 2, 3, 4, 5, 6, 7, 8]
    },
    'output': 0
}

# An empty list
test6 = {
    'input': {
        'nums': []
    },
    'output': 0
}

# A list with one element
test7 = {
    'input': {
        'nums': [1]
    },
    'output': 0
}

tests = [test0, test1, test2, test3, test4, test5, test6, test7]
for i, test in enumerate(tests):
    nums = test['input']['nums']
    expected = test['output']
    result = count_rotation_binary_search(nums)
    if result == expected:
        print(f"Test case {i} passed")
    else:
        print(f"Test case {i} failed. Expected {expected} but got {result}")
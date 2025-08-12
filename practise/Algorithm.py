def count_rotation(nums):
    print("received nums:", nums)
    return None

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
        'nums': [2, 3, 4, 5, 1]
    },
    'output': 1
}

# A list that is rotated n-1 times
test4 = {
    'input': {
        'nums': [2, 3, 4, 5, 6, 7, 8, 1]
    },
    'output': 1
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
print(tests)
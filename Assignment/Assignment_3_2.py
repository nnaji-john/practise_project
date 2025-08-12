"""
Assignment 3 Problem 2: Check valid chicken nugget combinations
July 27, 2025
Johnpaul Nnaji
"""

# Function to find valid combinations
def find_combinations(n):
    options = []
    for a in range(n // 6 + 1):
        for b in range(n // 9 + 1):
            for c in range(n // 22 + 1):
                if 6 * a + 9 * b + 22 * c == n:
                    combo = {
                        'Six_piece': a,
                        'Nine_piece': b,
                        'Twenty_two_piece': c
                    }
                    options.append(combo)
    return options


# Prompt for input
try:
    order_amount =int(input("How many chicken nuggets would you like to order? "))
except ValueError:
    print("Please enter a valid integer.")
    exit()

# Try original order
combinations = find_combinations(order_amount)


if combinations:
    print(f"For an order size of {order_amount}, choose from the following {len(combinations)} option(s):")
    for combo in combinations:
        print(combo)
else:
    print(f"Sorry, {order_amount} is not a feasible order size using box sizes of 6, 9, or 22.")
    # Find closest smaller valid number
    fallback = order_amount - 1
    while fallback > 0:
        combinations = find_combinations(fallback)
        if combinations:
            print(f"\nHowever, you have options for the closest smaller feasible order size:{fallback}")
            print(f"Here are {len(combinations)} option(s) you can choose from:")
            for combo in combinations:
                print(combo)
            break
        fallback -= 1
    else:
        print("No feasible combinations found below your requested size.")
"""
Assignment 3 Problem 3: Find the least expensive chicken nugget combination
July 27, 2025
Johnpaul Nnaji
"""

# Price dictionary
PRICES = {
    'Six_piece': 3,
    'Nine_piece': 4,
    'Twenty_two_piece':9
}


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


# Function to compute cost of a combination
def  calculate_cost(combo):
    return (
        combo['Six_piece'] * PRICES['Six_piece'] + 
        combo['Nine_piece'] * PRICES['Nine_piece'] +
        combo['Twenty_two_piece'] * PRICES['Twenty_two_piece']
    )


# Get user input
try:
    order_amount =int(input("How many chicken nuggets would you like to order? "))
except ValueError:
    print("Please enter a valid integer.")
    exit()


# Try original order
combinations = find_combinations(order_amount)

# If not valid, fallback to closet smaller
fallback = order_amount
while not combinations and fallback > 0:
    fallback -= 1
    combinations = find_combinations(fallback)


if combinations:
    #Find the least expensive option
    cheapest = min(combinations, key=calculate_cost)
    cost = calculate_cost(cheapest)
    print(f"\nLeast expensive option for {fallback} nugget(s):")
    print(cheapest)
    print(f"Total cost: ${cost}")
else:
    print("No feasible combinations found.")
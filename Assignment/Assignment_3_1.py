"""
Assignment 3 Problem 1: Check valid chicken nugget combinations
July 27, 2025
Johnpaul Nnaji
"""

try:
    order_amount =int(input("How many chicken nuggets would you like to order?"))
except ValueError:
    print("Please enter a valid integer.")
    exit()


valid_combinations = [] # store dictionaries of valid combinations


#Try all combinations of 6 piece, 9 piece, and 22 piece pasks
for a in range(order_amount // 6 + 1): # max max number of 6 piece pack
    for b in range(order_amount // 9 + 1): # max max number of 9 piece pack
        for c in range(order_amount // 22 + 1): # max max number of 22 piece pack
            total = 6 * a + 9 * b + 22 * c
            if total == order_amount:
                combo = {
                    'Six_piece': a,
                    'Nine_piece': b,
                    'Twenty_two_piece': c
                }
                valid_combinations.append(combo)
        

# Display results
if valid_combinations :
    print(f"For an order size of {order_amount}, choose from the following {len(valid_combinations)} option(s):")
    for option in valid_combinations :
        print(option)
else:
    print("Sorry, there is no valid combination using 6, 9, or 22 piece packs.")
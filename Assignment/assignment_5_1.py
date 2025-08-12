"""
Assignment 5 Problem 1: Retirement Plan - Fixed Growth Investment
August 6, 2025
Johnpaul Nnaji
"""

def fixedInvestor (salary, p_rate, f_rate, years):
    """
    A fixed retirement investment account growth over multiple years will look like.
    :param salary: Annual salary (float)
    :param p_rate: Employee contribution rate (decimal)
    :Param f_rate: fixed growth rate (decimal)
    :param years: Investment duration in years (int)
    :return: List of total retirement account vaules at end of each year
    """
    account_values = []

    # Determine match rate (max 5%)
    match_rate = min(p_rate, 0.05)

    # Total contribution per year = employee + employer + match
    annual_contribution = salary * (p_rate + 0.05 + match_rate)

    balance = 0
    for year in range(years):
            # Grow the previous balance
            balance = balance * (1 + f_rate) 
            # Add this year's contribution
            balance +=  annual_contribution
            # Store and round up to 2 decimal places
            account_values.append(round(balance, 2))
    
    return account_values




# ----------------------------
# Testing (comment out before submission)
# ----------------------------
# Example: salary = $50,000, p_rate = 0.05, f_rate = 0.05, years = 3
# Expected: [7500.0, 15375.0, 23643.75]
test_values = fixedInvestor(50000, 0.05, 0.05, 3)
print("Account values:", test_values)

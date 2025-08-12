"""
Assignment 5 Problem 3: Finally Retired - Simulating Retirement Drawdowns
August 6, 2025
Johnpaul Nnaji
"""

def finallyRetired(savings, r_rate, expenses):
    """
    Simulates a retirement account where money is withdrawn each year.
    
    :param savings: Initial savings at the start of retirement (float)
    :param r_rate: List of annual growth rates during retirement (list of floats)
    :param expenses: Annual expenses withdrawn at the end of each year (float)
    
    :return: List of account balances at the end of each year (after growth and expense withdrawal)
    """
    account_balances = []
    balance = savings

    for rate in r_rate:
        # Apply annual growth first
        balance *= (1 + rate)
        # Subtract expenses at end of year
        balance -= expenses
        # Round and store the result
        account_balances.append(round(balance, 2))

    return account_balances

# ----------------------------
# Testing (comment out before submission)
# ----------------------------
savings = 100000
r_rate = [0.05, 0.04, 0.03]
expenses = 25000
print("Year-end balances:", finallyRetired(savings, r_rate, expenses))
# Expected: [80000.0, 58200.0, 35946.0]

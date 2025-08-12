"""
Assignment 5 Problem 4: Determine max retirement expense using binary search
August 6, 2025
Johnpaul Nnaji
"""

def maximumExpensed(salary, p_rate, workRate, retiredRate, epsilon):
    """
    Uses binary search to estimate the maximum amount that can be expensed each year during retirement
    so that the retirement account is depleted to near-zero by the end of retirement.

    Parameters:
    - salary (float): Annual salary
    - p_rate (float): Employee contribution rate (e.g., 0.05 for 5%)
    - workRate (list of float): Annual return rates during working years
    - retiredRate (list of float): Annual return rates during retirement years
    - epsilon (float): Acceptable margin of error for remaining retirement balance

    Returns:
    - float: Maximum annual retirement expense
    """

    # Step 1: Compute savings after working years
    def variableInvestor(salary, p_rate, v_rate):
        balance = 0
        match_rate = min(p_rate, 0.05)
        annual_contribution = salary * (p_rate + 0.05 + match_rate)
        account_values = []

        for i in range(len(v_rate)):
            if i != 0:
                balance *= (1 + v_rate[i])
            balance += annual_contribution
            account_values.append(round(balance, 2))

        return account_values

    # Step 2: Simulate retirement withdrawals
    def finallyRetired(balance, r_rate, expense):
        for i in range(len(r_rate)):
            balance = balance * (1 + r_rate[i]) - expense
        return round(balance, 2)

    # Initial retirement savings from working years
    savings = variableInvestor(salary, p_rate, workRate)[-1]

    # Step 3: Binary search for max annual retirement expense
    low = 0
    high = savings
    guess = (high + low) / 2.0

    while abs(high - low) > epsilon:
        remaining = finallyRetired(savings, retiredRate, guess)
        print(f"Trying expense = ${round(guess, 2)}. Remaining balance = ${round(remaining, 2)}")

        if abs(remaining) <= epsilon:
            break
        elif remaining > 0:
            # Still money left, try higher expense
            low = guess
        else:
            # Overdrawn, try lower expense
            high = guess

        guess = (high + low) / 2.0

    return round(guess, 2)


# Test case
salary = 50000
p_rate = 0.05
workRate = [0.05, 0.04, 0.03]
retiredRate = [0.03, 0.02, 0.01, 0.01]
epsilon = 0.01

max_expense = maximumExpensed(salary, p_rate, workRate, retiredRate, epsilon)
print(f"Max sustainable expense per year in retirement: ${max_expense}")
